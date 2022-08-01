import email
from django.shortcuts import render, redirect
from .models import User
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def createUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
        return render(request, 'signup.html',{'form':form})

def signinPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			email = request.POST.get('email')
			password =request.POST.get('password')

			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'email or password is incorrect')

		context = {}
		return render(request, 'signin.html', context)

@login_required
def logoutUser(request):
	logout(request)
	return redirect('/')