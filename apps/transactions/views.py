from django.shortcuts import render

def showPageTransaction(request,idPass):
    context = {}
    return render(request,'show-page-transaction.html',context)

def doTransactionPass(request):
    return ''