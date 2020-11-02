from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BookModel

# Create your views here.
class BookListView(ListView):
    model = BookModel
    template_name = 'booklist.html'
    
class BookDetailView(DetailView):
    model = BookModel
    template_name = 'bookdetail.html'
