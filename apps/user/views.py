import email
from django.shortcuts import render, redirect
from .models import User, Wallet
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from SwimmingPoolDjangoConcept.decorators import administrator_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
import json

def createUser(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = UserCreationForm(request.POST or None)
		if form.is_valid():
			form.save()
			wallet = Wallet(user=User.objects.get(email=form.cleaned_data['email']))
			wallet.save()
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

@login_required(login_url='/user/signin')
def dashboard(request):
	balance = Wallet.objects.get(user=request.user)
	context = {
		"name" : request.user.nameUser,
		"surname" : request.user.surnameUser,
		"role" : request.user.get_role_display(),
		"balance" : balance.accountBalance
	}
	return render(request, 'dashboard.html', context)

@administrator_required
def setRole(request):
	context = {}
	return render(request, 'rule.html', context)

@administrator_required
@csrf_exempt
def setRoleForUser(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		emailData = body['email']
		roleData = body['newRole']
		try:
			user = User.objects.get(email=emailData)
			user.setRole(roleData)
			user.save()
			data = json.dumps("The user's role has been changed", cls=DjangoJSONEncoder)
		except:
			data = json.dumps("An internal server error has occurred.", cls=DjangoJSONEncoder)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

@administrator_required
@csrf_exempt
def getUsersList(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		emailData = body['email']
		user = User.objects.all().filter(Q(is_superuser=False) & Q(email__icontains=emailData))
		data = serializers.serialize('json', user,fields=('email','nameUser','surnameUser','role'))
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

@administrator_required
def getUser(request):
	if request.is_ajax():
		user = ""
		data = ''
		# data = json.dumps(user, cls=DjangoJSONEncoder)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

@login_required
def logoutUser(request):
	logout(request)
	return redirect('/')