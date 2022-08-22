from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect
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


class CartView(ListView):
    
    model = Book
    context_object_name = 'cart'
    template_name = 'wishlist.html'        