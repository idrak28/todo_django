from django.shortcuts import render
from .models import TODO
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView


class TODOListView(ListView):
    model = TODO
    template_name='todo_list.html'
    
    