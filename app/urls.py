from django.urls import path
from .views import TODOListView ,TODOFormView
urlpatterns = [
    path('', TODOListView.as_view(), name='todo_list'),
    path('form',TODOFormView.as_view(),name='todo_form'),
  
] 