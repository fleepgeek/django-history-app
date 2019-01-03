from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
from history.mixins import ObjectViewMixin

class PostList(ListView):
    model = Post

class PostDetail(ObjectViewMixin, DetailView):
    model = Post