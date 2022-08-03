import email
from django.shortcuts import render, redirect
from .models import User
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from SwimmingPoolDjangoConcept.decorators import administrator_required
from django.core.serializers.json import DjangoJSONEncoder
import json

def createUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/user/signin/')
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

# @administrator_required
def setRule(request):
	context = {}
	return render(request, 'rule.html', context)

# @administrator_required
def getUsersList(request):
	if request.is_ajax():
		user = User.objects.filter().all()
		data = json.dumps(list(user), cls=DjangoJSONEncoder)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

# @administrator_required
def getUser(request):
	if request.is_ajax():
		user = ""
		data = json.dumps(list(user), cls=DjangoJSONEncoder)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

@login_required
def logoutUser(request):
	logout(request)
	return redirect('/')