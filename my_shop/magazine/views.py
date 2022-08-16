from django.shortcuts import render
from django.views.generic import ListView


#from .models import magaz


#class ListView(ListView):

   # model = magaz
    #template_name = 'base.html'


#def index(request):
    #tovar = magaz.objects.all()
    #return render(request, "popular.html",{'tovar' : tovar})    

def home(request):
    return render(request, 'base.html')
    