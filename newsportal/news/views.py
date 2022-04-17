from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


class PostList(ListView):
   model = Post
   context_object_name = 'news'
   template_name = 'news.html'
   queryset = Post.objects.order_by('-id')


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'


class Post(DetailView):
    model = Post
    context_object_name = 'Post'



