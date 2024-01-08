from ticket_app.models import Entry

for i in range(1000, 1100):
    ticket_id = f"XXX-{i}-KY24"
    ticket_profile = Entry.objects.create(ticket_id=ticket_id,
                                              day = 2,
                                              entry_done = False)
    ticket_profile.save()

for object in Entry.objects.all():
    object.entry_done = False
    object.save()