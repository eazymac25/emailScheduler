# hello

from django.shortcuts import render, redirect
from email_app.forms import EmailForm
from django.http import HttpResponseRedirect

def add_email(request):
	pass
	if request.method == 'POST':
		form = EmailForm(request.POST)

		if form.is_valid():
			print(form.cleaned_data)
			#return HttpResponseRedirect('/thanks/')
	else:
		form = EmailForm()
	return render(request, 'email_form.html', {'form': form})