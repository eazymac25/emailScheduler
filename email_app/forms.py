# forms.py
from django import forms


class EmailForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	your_email = forms.CharField(label='Your email', max_length=100)