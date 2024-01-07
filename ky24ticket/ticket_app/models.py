from django.db import models

# Create your models here.

day_choices = [
    (None, 'day'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
]
class Entry(models.Model):
    ticket_id = models.CharField(max_length=20, null=True, blank=True)
    day = models.PositiveIntegerField(choices=day_choices, null=True, blank=True)
    entry_done = models.BooleanField(default=False)
