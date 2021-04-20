from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            'message from' +' '+ name +' '+ email,
            message,
            email,
            ['artur199933@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'wwwapp/home.html', {'name': name})
    else:
        return render(request, 'wwwapp/home.html')


# def profile(request):
#     return render(request, 'wwwapp/profile.html')
#
#
# def about(request):
#     return render(request, 'wwwapp/update_task.html')
