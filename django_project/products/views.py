from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product
from history.mixins import ObjectViewMixin

class ProductList(ListView):
    model = Product


class ProductDetail(ObjectViewMixin, DetailView):
    model = Product