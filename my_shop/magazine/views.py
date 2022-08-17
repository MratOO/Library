from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Book, Genres


class ListView(ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'book_list.html'
    
    def get_queryset(self):
        return Book.objects.filter(genre__slug=self.kwargs.get('slug'))

class BookDetailView(DetailView):

    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'        
    template_name = 'book_detail.html'
      


class HomeView(ListView):
    
    model = Book
    template_name = 'home.html' 


    