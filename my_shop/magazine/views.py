from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


from .models import Book, Genres
from .forms import *


class ListView(ListView):

    model = Book
    context_object_name = 'book_list'
    slug_url_kwarg = 'list_slug'
    template_name = 'books/book_list.html'
    
    def get_queryset(self):
        return Book.objects.filter(genre__slug=self.kwargs.get('list_slug'))

class BookDetailView(DetailView):

    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'        
    template_name = 'books/book_detail.html'
      


class HomeView(ListView):
    
    model = Book
    context_object_name = 'home'
    template_name = 'books/home.html' 

class RegisterUser(CreateView):
    
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')