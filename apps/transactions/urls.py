from django.urls import path

from . import views


urlpatterns = [
    path('buyPass/<int:idPass>/', views.showPageTransaction, name='transactions-buy-pass'),
]