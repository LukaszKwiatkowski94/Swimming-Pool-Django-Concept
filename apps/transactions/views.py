from django.shortcuts import render
from django.http import Http404, HttpResponse
from apps.user.models import User, Wallet
from apps.offers.models import Passes
from apps.clientHistory.models import ClientHistoryPasses
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import json

def showPageTransaction(request,idPass):
    try:
        wallet = Wallet.objects.get(user = request.user)
        passBuy = Passes.objects.get(id=idPass)
        context = {
            'balanceNow':wallet.accountBalance,
            'passBuy':passBuy,
            'balanceAfter':(wallet.accountBalance-passBuy.price)
        }
        return render(request,'show-page-transaction.html',context)
    except:
        raise Http404("Transaction does not exist")

@csrf_exempt
def doTransactionPass(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        userID = body['user']
        passId = body['passId']
        try:
            userObj = User.objects.get(id=userID)
            wallet = Wallet.objects.get(user=userObj)
            passObj = Passes.objects.get(id=passId)
            if((wallet.accountBalance-passObj.price)>0):
                endDate = datetime.today() + timedelta(days=passObj.daysOfUse)
                newPassForUser = ClientHistoryPasses(user=userObj,passID=passObj,dateEnd=endDate)
                newPassForUser.save()
                wallet.accountBalance = wallet.accountBalance - passObj.price
                wallet.save()
                data = json.dumps("success", cls=DjangoJSONEncoder)
            else:
                data = json.dumps("You don't have enough money.", cls=DjangoJSONEncoder)
        except:
            data = json.dumps("Problem with transactions. ", cls=DjangoJSONEncoder)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404