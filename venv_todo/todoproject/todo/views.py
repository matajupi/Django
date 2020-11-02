from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class TodoView(ListView):
    model = TodoModel
    template_name = 'list.html'

class TodoDetailView(DetailView):
    model = TodoModel
    template_name = 'detail.html'

class TodoCreateView(CreateView):
    model = TodoModel
    template_name = 'create.html'
    fields = ['title', 'content', 'pic']
    success_url = reverse_lazy('list')

class TodoDeleteView(DeleteView):
    model = TodoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')

class TodoUpdateView(UpdateView):
    model = TodoModel
    template_name = 'update.html'
    fields = ['title', 'content', 'pic']
    success_url = reverse_lazy('list')
