from django import forms
from .models import TODO
from django.shortcuts import render
#from django.forms import ModelForm, Textarea


class TODOForm(forms.ModelForm):
  
  class Meta:
    model = TODO
    
    fields = ['text', 'deadline_at']
    widgets = {
            'deadline_at':forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}),
            
        }
  