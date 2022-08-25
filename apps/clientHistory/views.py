from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import ClientHistoryPasses
from apps.user.models import User
from django.contrib.auth.decorators import login_required
import json
import datetime;

@login_required
def showMyHistory(request):
    try:
        historyPasses = ClientHistoryPasses.objects.filter(user=request.user).order_by('-id')
        context = {
            'historyPasses':historyPasses,
            'date':datetime.date.today()
        }
    except:
        raise Http404("Client History Passes does not exist")
    return render(request,'showHistoryClient.html', context)

@login_required
def showClientHistory(request,idUser):
    try:
        historyPasses = ClientHistoryPasses.objects.filter(user=idUser).order_by('-id')
        context = {
            'historyPasses':historyPasses,
            'date':datetime.date.today()
        }
    except:
        raise Http404("Client History Passes does not exist")
    return render(request,'showHistoryClient.html', context)

@login_required
def createNewPassRecord(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        idUser = body['idUser']
        idPass = body['passId']
        dateEndPost = body['dateEnd']
        newRecord = ClientHistoryPasses(user=idUser,passID=idPass,dateEnd=dateEndPost)
        newRecord.save()
    else:
        raise Http404("Client History Passes does not exist")
