from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.createUser), # creating a user
    path('signin/', views.signinPage), # login
    path('logout/', views.logoutUser), # logout User
    path('setRole/', views.setRole), # set rule for user
    path('setRoleForUser/', views.setRoleForUser), # JS Request set rule for user
    path('getUsersList/', views.getUsersList), # JS Request for get users List
    path('getUser/', views.getUser) # JS Request for get user
]