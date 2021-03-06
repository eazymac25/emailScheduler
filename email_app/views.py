# hello

from django.shortcuts import render, redirect
from email_app.forms import EmailForm, NotificationForm, SignUpForm
from django.http import HttpResponseRedirect

def add_email(request):
	if request.method == 'POST':
		form = NotificationForm(request.POST)

		if form.is_valid():
			print(form.cleaned_data)
			form = NotificationForm()
			#return HttpResponseRedirect('/thanks/')
	else:
		form = NotificationForm()
	return render(request, 'email_form.html', {'form': form})


def create_user(request):
	pass


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		next_url = '/'
		try:
			next_url = request.POST['next']
		except KeyError as e:
			print('next paramter DNE')
		return redirect(next_url)
	else:
		form = SignUpForm()
	return render(request, 'signup/signup.html', {'form': form})