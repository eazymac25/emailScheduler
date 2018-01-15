# hello

from django.shortcuts import render, redirect
from email_app.forms import EmailForm, NotificationForm
from django.http import HttpResponseRedirect

def add_email(request):
	pass
	if request.method == 'POST':
		form = NotificationForm(request.POST)

		if form.is_valid():
			print(form.cleaned_data)
			form = NotificationForm()
			#return HttpResponseRedirect('/thanks/')
	else:
		form = NotificationForm()
	return render(request, 'email_form.html', {'form': form})