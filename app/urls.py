from django.urls import path
from .views import TODOListView
urlpatterns = [
    path('', TODOListView.as_view(), name='todo_list'),
  
] 