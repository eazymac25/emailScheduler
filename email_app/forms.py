# forms.py
from django import forms
from email_app.models import Notification


class EmailForm(forms.Form):
	"""
	For to define a simple email for testing post functionality
	"""
	your_name = forms.CharField(label='Your name', max_length=100)
	your_email = forms.CharField(label='Your email', max_length=100)


class NotificationForm(forms.Form):
	"""
	This form should be a row in a table of notifications that a user
	can manage from a notification table
	"""

	EVENT_LIST = (
		(0, "--- None ---"),
		(1, "Birthday"),
		(2, "Christmas"),
	)

	# define time periods in seconds
	DAY = 86400
	WEEK = 604800
	MONTH = 2629746
	YEAR = 31557600

	RECUR_OPTS = (
		(YEAR, 'YEARLY'),
		(MONTH, 'MONTHLY'),
		(WEEK, 'WEEKLY'),
		(DAY, 'DAILY'),
	)

	recipient_first_name = forms.CharField(label='Recipient First Name', max_length=100)
	recipient_relationship = forms.CharField(label='Relationship', max_length=100)
	event = forms.ChoiceField(label='Event', widget=forms.Select(), choices=EVENT_LIST)
	start_date = forms.DateField(label='Start Date')
	end_date = forms.DateField(label='End Date')
	repeat = forms.IntegerField(label='Repeat')
	recurrance = forms.ChoiceField(label='Recurrance', choices=RECUR_OPTS)

class ModelNotificationForm(forms.ModelForm):
	"""
	We probably can't use the built in modelform because we introduced complexity into the 
	Notification data model by splitting everything into multiple tables
	"""
	class Meta:
		model = Notification
		fields = ['recipient']




