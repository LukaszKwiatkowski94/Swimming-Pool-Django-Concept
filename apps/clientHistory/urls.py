from django.urls import path

from . import views


urlpatterns = [
    path('', views.showMyHistory, name='my-client-history'),
    path('clientHistory/', views.showClientHistory, name='client-history'),
    path('createNewPassRecord/', views.createNewPassRecord, name='create-new-pass-record')
]