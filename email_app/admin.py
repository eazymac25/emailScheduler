from django.contrib import admin

# Register your models here.
from email_app.models import EmailUser, Relationship, Recipient, Recur, EventType, Event

admin.site.register(EmailUser)
admin.site.register(Relationship)
admin.site.register(Recipient)
admin.site.register(Recur)
admin.site.register(Event)
admin.site.register(EventType)