from django.shortcuts import render,HttpResponse
from cryptography.fernet import Fernet
from rest_framework.response import Response
from rest_framework import status
from ticket_app.models import *

def entry(request):
    print("View triggered")
    print(request)
    # we will be encrypting the below string.
    message = request.msg
    
    # generate a key for encryption and decryption
    # You can use fernet to generate 
    # the key or use random key generator
    # here I'm using fernet to generate key
    
    key = Fernet.generate_key()
    
    # Instance the Fernet class with the key
    
    fernet = Fernet(key)
    print("key", key)
    
    # then use the Fernet class instance 
    # to encrypt the string string must
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
    
    print("original string: ", message)
    print("encrypted string: ", encMessage)

    print("================================================")
    # decrypt the encrypted string with the 
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods
    # encMessage = "gAAAAABlmknwlXHae_T4mmgQwXPWDzj97MlFZlmEmvzfVs-yAaVo-vPtW646ZUsbMhKtEFYR2KubilN39-WL7wwbKQ_5NRi6_Q=='"
    try:
        decMessage = fernet.decrypt(encMessage).decode()
        
        print("decrypted string: ", decMessage)
        ticket_id = decMessage['id']
        day = decMessage['day']
        ticket_profile = Entry.objects.create(ticket_id=ticket_id,
                                              day = day,
                                              entry_done = True)
        ticket_profile.save()
        return Response({"msg": "Successfull"}, status=status.HTTP_200_OK)
    except:
        print("bhag bc")
        return Response({"msg": "Invalid access"}, status=status.HTTP_404_NOT_FOUND)
# Create your views here.
