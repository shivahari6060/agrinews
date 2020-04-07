from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


from django.contrib import messages

# Create your views here.

def register(request):
	form = CreateUserForm()
 
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for   ' + user)
			return redirect('login')



	context = {
	'form': form,
	}
	return render(request, 'accounts/register.html', context)


# this is the login page 

def loginPage(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('Blog')

		else:
			messages.info(request, 'Username or Password is incorrect')

	context ={

	}

	return render(request, 'accounts/login.html', context)

# here is the logout function

def logoutUser(request):
	logout(request)
	return redirect('login')
