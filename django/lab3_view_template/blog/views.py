from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def year_archive(request, year):
    posts = Post.objects.filter(created_at__year=year)
    return render(request, 'blog/year_archive.html', {'year': year, 'posts': posts})

