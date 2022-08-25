from django.shortcuts import render
from apps.user.models import User, Wallet
from apps.offers.models import Passes

def showPageTransaction(request,idPass):
    wallet = Wallet.objects.get(user = request.user)
    passBuy = Passes.objects.get(id=idPass)
    context = {
        'balanceNow':wallet.accountBalance,
        'passBuy':passBuy,
        'balanceAfter':(wallet.accountBalance-passBuy.price)
    }
    return render(request,'show-page-transaction.html',context)

def doTransactionPass(request):
    return ''