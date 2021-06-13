from django.urls import path, reverse_lazy
from users import views as user_views
from django.contrib.auth import views as auth_views
from blog.views import LoginView
from django.urls import reverse_lazy


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', next_page=reverse_lazy('blog-home')),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
