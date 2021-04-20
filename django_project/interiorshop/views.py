from django.shortcuts import render


def frontpage(request):
    return render(request, 'interiorshop/frontpage.html')


def contact(request):
    return render(request, 'interiorshop/contact.html')