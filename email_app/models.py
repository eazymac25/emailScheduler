from django.db import models
from django.contrib.auth.models import User

class EmailUser(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.CharField(max_length=100)


class Relationship(models.Model):

	name = models.CharField(max_length=100, help_text='Enter exhaustive list of supported relationships')


class Recipient(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.CharField(max_length=100)
	email_user = models.ForeignKey('EmailUser', on_delete=models.SET_NULL, null=True)
	relationship = models.ForeignKey('Relationship', on_delete=models.SET_NULL, null=True)

class Recur(models.Model):

	name = models.CharField(max_length=100)

class EventType(models.Model):

	name = models.CharField(max_length=100)


class Event(models.Model):

	event_type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True)
	event_name = models.CharField(max_length=100)
	recur = models.ForeignKey('Recur', on_delete=models.SET_NULL, null=True)


class Notification(models.Model):
	pass


