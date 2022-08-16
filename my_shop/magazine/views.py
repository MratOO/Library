from django.shortcuts import render
from django.views.generic import ListView


from .models import Book


class ListView(ListView):

    model = Book
    template_name = 'book_list.html'
    
    def get_queryset(self):
        return Book.objects.filter(genre__slug=self.kwargs.get('slug'))


def home(request):
    return render(request, 'base.html')    


    