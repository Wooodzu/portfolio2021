from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todohome, name='todo-home'),
    path('todo/update_task/<str:pk>/', views.updateTask, name='todo-update_task'),
    path('todo/delete/<str:pk>/', views.deleteTask, name='todo-delete'),

]
