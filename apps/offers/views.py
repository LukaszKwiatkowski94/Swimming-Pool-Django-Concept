from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import Passes
from .forms import PassForm
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from SwimmingPoolDjangoConcept.decorators import accountant_required
import json

def show(request):
    try:
        passes = Passes.objects.filter(active=True)
        context = {
            'passes':passes
        }
        return render(request,'show-offers.html',context)
    except:
        raise Http404("Get Passes does not exist")

@login_required
@accountant_required
def createPass(request):
    try:
        form = None
        if request.POST:
            form = PassForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = PassForm()
            context = {
                'form':form,
                'name':"create"
            }
        return render(request, 'create-update-offers.html',context)
    except:
        raise Http404("Create Pass does not exist")

@login_required
@accountant_required
def updatePass(request,idPass):
    try:
        form = None
        passItem = Passes.objects.get(id=idPass)
        if request.POST:
            form = PassForm(request.POST)
            obj = form.save(commit=False)
            if form.is_valid() and (passItem.namePass != obj.namePass or passItem.daysOfUse != obj.daysOfUse or passItem.price != obj.price):
                passItem.active = False
                passItem.save()
                newPass = Passes(namePass=obj.namePass,daysOfUse=obj.daysOfUse,price=obj.price)
                newPass.save()
            return redirect('/')
        else:
            form = PassForm(instance=passItem)
            context = {
                'form':form,
                'name':"update"
            }
        return render(request, 'create-update-offers.html',context)
    except:
        raise Http404("Update Pass does not exist")

@login_required
@accountant_required
def showAllListPasses(request):
    try:
        passes = Passes.objects.all().order_by('active')
        context = {
            'passes':passes
        }
        return render(request,'showAllListPasses.html',context)
    except:
        raise Http404("Passes does not exist")

@login_required
@accountant_required
def deactivatePass(request):
    if request.POST:
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            idPass = body['idPass']
            post = Passes.objects.get(id=idPass)
            post.active != post.active
            post.save()
            data = json.dump(post.active, cls=DjangoJSONEncoder)
        except:
            data = json.dump('Error', cls=DjangoJSONEncoder)
        return HttpResponse(data,content_type='application/json')
    else:
        raise Http404("Passes does not exist")