from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
import datetime

# Create your views here.
def index(request):
    blog = Blog.objects
    return render(request, 'index.html', {'blogs':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.like = request.GET['like']
    blog.save()
    return redirect('/')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'blog':blog})

def ud(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.like = request.GET['like']
    blog.date = datetime.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog_id))

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')
