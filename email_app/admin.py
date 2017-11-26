from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from email_app.models import Relationship, Recipient, EventType, Event, Notification

admin.site.register(Relationship)
admin.site.register(Recipient)
admin.site.register(Event)
# admin.site.register(EventType)
admin.site.register(Notification)

################## Redo Base User Forms #####################
class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name')  # etc...

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('first_name', 'last_name'), "classes": ("wide",)}),)
# don't forget to register your custom admin class
admin.site.unregister([User])
admin.site.register(User, MyUserAdmin)
############################################################

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
	"""
	Quick and dirty event type admin view
	"""
	list_display = ('name',)
	fields = ['name']