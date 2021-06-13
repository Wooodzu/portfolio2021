from django.shortcuts import render
from product.models import Product
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url


def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    return render(request, 'interiorshop/frontpage.html', {'newest_products': newest_products})


def contact(request):
    return render(request, 'interiorshop/contact.html')


class LoginView(auth_views.LoginView):
    next_page = None

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)