from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
from interiorshop.views import LoginView
from django.urls import reverse_lazy


urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('logout/', auth_views.LogoutView.as_view(template_name='vendor/logout.html'), name='loggout'),
    path('login/', LoginView.as_view(template_name='vendor/login.html', next_page=reverse_lazy('frontpage')), name='loggin'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
]