from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('add-contact/', views.addContact, name='new'),
    path('profile/<str:pk>', views.contactProfile, name='profile'),
    path('edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('delete/<str:pk>', views.deleteContact, name='delete'),
]