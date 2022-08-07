from django.urls import path

from . import views


urlpatterns = [
    path('', views.showMainPage, name='blog'),
    path('page/<numberPage>/', views.showBlogPage, name='blog-page'), 
    path('post/<idPost>/', views.showPost, name='get-blog-post'),
    path('create/', views.create, name='create-blog-post'),
    path('update/<idPost>/', views.update, name='update-blog-post'),
    path('giveLike/', views.giveLike, name='give-like-blog-post'),
    path('allPosts/', views.getAllPosts, name='all-blog-post')
]