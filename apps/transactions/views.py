from django.shortcuts import render
from django.http import Http404, HttpResponse
from apps.user.models import User, Wallet
from apps.offers.models import Passes

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

def doTransactionPass(request):
    return ''