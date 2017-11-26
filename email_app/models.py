from django.db import models
from django.contrib.auth.models import User
from django_unixdatetimefield import UnixDateTimeField

class Recipient(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	relationship = models.ForeignKey('Relationship', on_delete=models.SET_NULL, null=True)


class Relationship(models.Model):

	name = models.CharField(max_length=100, help_text='Enter exhaustive list of supported relationships')


class EventType(models.Model):

	name = models.CharField(max_length=100)


class Event(models.Model):

	event_type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True)
	event_name = models.CharField(max_length=100)


class Notification(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	recipient = models.ForeignKey('Recipient', on_delete=models.SET_NULL, null=True)
	event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	next_notify_date = UnixDateTimeField(null=True)
	max_repeats = models.IntegerField(null=True)
	notify_count = models.IntegerField(null=True, default=0)

	# define active vs inactive chars
	ACTIVE = 'Y'
	INACTIVE = 'N'

	IS_ACTIVE_OPTS = (
		(ACTIVE, 'ACTIVE'),
		(INACTIVE, 'INACTIVE')
	)

	is_active = models.CharField(max_length=1, choices=IS_ACTIVE_OPTS, default=ACTIVE)

	# define time periods in seconds
	DAY = 86400
	WEEK = 604800
	MONTH = 2629746
	YEAR = 31557600

	RECUR_OPTS = (
		(DAY, 'DAILY'),
		(WEEK, 'WEEKLY'),
		(MONTH, 'MONTHLY'),
		(YEAR, 'YEARLY')
	)

	recurrance = models.IntegerField(choices=RECUR_OPTS, default=YEAR)


