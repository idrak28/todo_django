from django.urls import path
from .views import TODOListView ,TODOFormView ,TODOUpdateView ,TaskDelete
urlpatterns = [
    path('', TODOListView.as_view(), name='todo_list'),
    path('form',TODOFormView.as_view(),name='todo_form'),
    
    path('<pk>/update', TODOUpdateView.as_view(),name="todo_update"),
    path('<pk>/delete', TaskDelete.as_view(),name="todo_delete"),
] 