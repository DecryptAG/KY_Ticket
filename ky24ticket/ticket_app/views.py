from django.shortcuts import render,HttpResponse
from cryptography.fernet import Fernet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ticket_app.models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@api_view(('POST',))
@csrf_exempt
def entry(request):
    print("View triggered")
    print(request)
    # we will be encrypting the below string.
    message = request.POST.get("data")
    print(message)
    
    # generate a key for encryption and decryption
    # You can use fernet to generate 
    # the key or use random key generator
    # here I'm using fernet to generate key
    key = settings.ENC_KEY
    fernet = Fernet(key)
    print("key",key)
    
    try:
        decMessage = fernet.decrypt(message).decode()
        
        print("decrypted string: ", decMessage)
        e = Entry.objects.get(ticket_id=decMessage)

        if e.day != 1:
            return Response({"msg": "Not todays pass"}, status=status.HTTP_403_FORBIDDEN)
        
        elif (e.entry_done == True):
            return Response({"msg": "Entry already done"}, status=status.HTTP_403_FORBIDDEN)

        else:
            e.entry_done = True
            e.save()
            return Response({"msg": "Successfull"}, status=status.HTTP_200_OK)

        
    except:
        return Response({"msg": "Invalid access"}, status=status.HTTP_403_FORBIDDEN)
# Create your views here.
