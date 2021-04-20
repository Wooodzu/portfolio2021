from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wwwapp-home'),
    #path('profile/', views.profile, name='wwwapp-profile'),
    #path('about/', views.about, name='wwwapp-about'),
]