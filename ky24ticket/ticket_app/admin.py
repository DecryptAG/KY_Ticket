from django.contrib import admin

from ticket_app.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('ticket_id',"day")
    list_filter = ()


admin.site.register(Entry, EntryAdmin)
# Register your models here.
