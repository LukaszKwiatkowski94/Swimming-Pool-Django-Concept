from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.createUser, name='sign-up'), # creating a user
    path('signin/', views.signinPage, name='sign-in'), # login
    path('logout/', views.logoutUser, name='log-out'), # logout User
    path('setRole/', views.setRole, name='set-role'), # set rule for user
    path('setRoleForUser/', views.setRoleForUser), # JS Request set rule for user
    path('getUsersList/', views.getUsersList), # JS Request for get users List
    # path('getUser/', views.getUser) # JS Request for get user
    path('dashboard/', views.dashboard, name='dashboard') # JS Request for get user
]