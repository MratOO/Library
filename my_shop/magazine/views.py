from django.http import HttpResponse
from django.views.generic import ListView

from .models import magaz


class ListView(ListView):

    model = magaz
    template_name = 'base.html'


    