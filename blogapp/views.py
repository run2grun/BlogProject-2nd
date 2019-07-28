from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

def home(request):
    blogs=Blog.objects.all().order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    
    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/edit.html', {'blog':blog} )

def update(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect ('home')

# Create your views here.

