from django.shortcuts import render

def showPageTransaction(request):
    context = {}
    return render(request,'show-page-transaction.html',context)

def doTransactionPass(request):
    return ''