from django.urls import path

from . import views


urlpatterns = [
    path('', views.show, name='offers'),
    path('createPass/', views.createPass, name='create-pass'),
    path('updatePass/<int:idPass>/', views.updatePass, name='update-pass'),
    path('listPass/', views.showAllListPasses, name='show-all-list-passes')
]