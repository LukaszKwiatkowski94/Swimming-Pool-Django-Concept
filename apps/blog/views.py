from django.http import Http404, HttpResponse
from django.shortcuts import render , redirect
from django.core.serializers.json import DjangoJSONEncoder
from .models import BlogPosts
from .forms import PostCreationForm
import json

PAGE_POSTS = 5

def showMainPage(request):
    try:
        posts = BlogPosts.objects.filter(published=True).order_by('-id')[:PAGE_POSTS]
        context = {
            'posts': posts
        }
    except BlogPosts.DoesNotExist:
        raise Http404("BlogPosts does not exist")
    return render(request, 'blog.html', context)

def showBlogPage(request,nuberPage):
    try:
        start = (nuberPage-1)*PAGE_POSTS
        end = start + PAGE_POSTS
        posts = BlogPosts.objects.filter(published=True).order_by('-id')[start:end]
        context = {
            'posts': posts
        }
    except BlogPosts.DoesNotExist:
        raise Http404("BlogPosts does not exist")
    return render(request, 'blog.html', context)

def showPost(request,idPost):
    try:
        post = BlogPosts.objects.get(id=idPost)
        context = {
            'post': post
        }
    except BlogPosts.DoesNotExist:
        raise Http404("BlogPosts does not exist")
    return render(request, 'post.html', context)

def create(request):
    try:
        form = None
        if request.POST:
            form = PostCreationForm(request.POST or None, request.FILES)
            print(request.POST)
            print("###################")
            print(form.errors.as_data())
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
                return redirect('/blog')
        if form is None:
            form = PostCreationForm()
            context = {
                'form':form,
                'name':"create"
            }
        return render(request, 'create-update.html',context)
    except:
        raise Http404("Createation Post does not exist")

def update(request,idPost):
    try:
        post = BlogPosts.objects.get(id=idPost)
        form = PostCreationForm(request.POST or None,instance=post)
        context = {
            'form':form,
            'name':"update"
        }
        if form.is_valid():
            form.save()
            return redirect('/blog/post/'+form.id+'/')
        return render(request, 'create-update.html',context)
    except:
        raise Http404("Createation Post does not exist")

def giveLike(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            idPost = body['idPost']
            post = BlogPosts.objects.get(id=idPost)
            post.giveLike()
            post.save()
            data = json.dump(post.liked, cls=DjangoJSONEncoder)
        except:
            data = json.dump('Error', cls=DjangoJSONEncoder)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404("Give Like for post does not exist")

def getAllPosts(request):
    try:
        posts = BlogPosts.objects.filter(published=True).order_by('-id')
        context = {
            'posts': posts
        }
    except BlogPosts.DoesNotExist:
        raise Http404("BlogPosts does not exist")
    return render(request, 'allPosts.html', context)          