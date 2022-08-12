from django.urls import path

from . import views


urlpatterns = [
    path('', views.showMainPage, name='blog'),
    path('page/<int:nuberPage>/', views.showPage, name='blog-page'), 
    path('post/<int:idPost>/', views.showPost, name='get-blog-post'),
    path('create/', views.create, name='create-blog-post'),
    path('update/<int:idPost>/', views.update, name='update-blog-post'),
    path('giveLike/', views.giveLike, name='give-like-blog-post'),
    path('allPosts/', views.getAllPosts, name='all-blog-post')
]