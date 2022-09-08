from email import contentmanager
from turtle import title
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


from .models import Author, Book, Genres
from .forms import *


class ListView(ListView):

    paginate_by = 6
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        return context
      
      
class HomeView(ListView):
    
    model = Book
    context_object_name = 'home'
    template_name = 'books/home.html' 

class RegisterUser(CreateView):
    
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home') 

class LoginUser(LoginView):

    form_class = AuthenticationForm
    template_name = 'users/login.html'

def logout_user(request):
    logout(request)
    return redirect('login')
      
class CreateReview(CreateView):
    
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()
        return redirect(book.get_absolute_url(), {'review':book})

class Search(ListView):

    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
        
class AuthorDetailView(DetailView):

    model = Author
    context_object_name = 'author' 
    slug_url_kwarg = 'author_slug'    
    template_name = 'author_detail.html' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['books'] = Book.objects.filter(author__slug=self.kwargs.get('author_slug'))
        return context
      
class GenreListView(ListView):

    model = Genres
    context_object_name = 'genres_list'
    slug_url_kwarg = 'genre_slug'
    template_name = 'books/book_list.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genres'] = Genres.objects.all()
        return context