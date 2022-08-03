from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.createUser), # creating a user
    path('signin/', views.signinPage), # login
    path('logout/', views.logoutUser), # logout User
    path('setRule/', views.setRule), # set rule for user
    path('getUsersList/', views.getUsersList), # Ajax Request for get users List
    path('getUser/', views.getUser) # Ajax Request for get user
]