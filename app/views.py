from django.shortcuts import render
from .models import TODO
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import TODOForm
from django.contrib.auth.decorators import login_required  #login
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login 
class TODOListView(ListView):
    model = TODO
    template_name='todo_list.html'
    
 

class TODOFormView(FormView):
    template_name = "todo_form.html"
    form_class = TODOForm
    model = TODO
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo_list')
    
    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user
        todo.save()
        return super(TODOFormView,self).form_valid(form)
    
        
    