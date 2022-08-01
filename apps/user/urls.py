from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.createUser), # creating a user
    path('signin/', views.signinPage), # login
    path('logout/', views.logoutUser), # logout User
]