from django.shortcuts import render
from .models import TODO
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import TODOForm
from django.contrib.auth.decorators import login_required  #login
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login 

from django.contrib import messages 
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
    
    
class TODOUpdateView(UpdateView):
    model=TODO
    template_name = "todo_update.html"
    #queryset =TODO.objects.datetimes()
    fields =[
        "text",
        "deadline_at" ,
    ]        
    success_url ="/"
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TODOUpdateView,self).form_valid(form)
class TaskDelete(DeleteView):
    model = TODO
    template_name = "todo_delete.html"
    success_url ='/'
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)
