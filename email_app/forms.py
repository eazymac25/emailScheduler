# forms.py
from django import forms


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

	recipient_first_name = forms.CharField(label='Recipient First Name', max_length=100)
	recipient_relationship = forms.CharField(label='Relationship', max_length=100)
	event = forms.ChoiceField(label='Event', widget=forms.Select(), choices=self.EVENT_LIST, default=0)
	start_date = forms.DateField()