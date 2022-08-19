from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import ClientHistoryPasses
from user.models import User
import json

def showMyHistory(request):
    try:
        historyPasses = ClientHistoryPasses.objects.filter()
        context = {
            'historyPasses':historyPasses
        }
    except:
        raise Http404("Client History Passes does not exist")
    render(request,'showHistoryClient.html', context)

def showClientHistory(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        idUser = body['idUser']
        userObj = User.objects.get(id=idUser)
        history = ClientHistoryPasses.objects.filter(user=userObj)
        data = serializers.serialize('json', history)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404("Client History Passes does not exist")

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
