from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            'message from' + ' ' +str(name) + ' ' + email,
            message,
            email,
            ['artur199933@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'wwwapp/home.html', {'name': name})
    else:
        return render(request, 'wwwapp/home.html')



