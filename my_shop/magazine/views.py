from email import contentmanager
from turtle import title
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
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
      
class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()
        return redirect(book.get_absolute_url(), {'review':book})      

class BooksView(View):

    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/all_books.html', {'books':books})

class Search(ListView):

    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context