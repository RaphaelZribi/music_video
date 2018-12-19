from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms


def log_in(request):
	if request.user.is_authenticated:
		return redirect(reverse('main_app:home'), permanent=False)

	errors = False
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			clean_data = login_form.clean()
			user = authenticate(username=clean_data['username'], password=clean_data['password'])

			if user is not None:
				login(request, user)
				print('Logged In: {}'.format(user))
				return redirect(reverse('main_app:home'), permanent=False)
				
			else:
				errors = True
	else:
		login_form = forms.LoginForm()

	return render(request, 'login.html', {
			'login_form': login_form,
			'errors': errors,})


def signup(request):

	if request.user.is_authenticated:
		return redirect(reverse('main_app:home'), permanent=False)
	



	registered = False
	if request.method =='POST':
		user_form = forms.UserForm(data= request.POST) 
		profile_form = forms.UserProfileForm(data= request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit= False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
			
			profile.save()
			registered = True
			login(request, user)
			return redirect(reverse('main_app:home'), permanent=False)



		else : 
			print(user_form.errors, profile_form.errors)

	else: 
		user_form = forms.UserForm()
		profile_form = forms.UserProfileForm()

	return render(request, 'signup.html', context = {
		'user_form' : user_form,
		'profile_form' : profile_form, 
		'registered': registered
		})
