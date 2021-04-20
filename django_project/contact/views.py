from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'contact/contact.html', {'contacts': contacts, 'search_input': search_input})



def addContact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')

    context = {'form': form}
    return render(request, 'contact/new.html', context)


def contactProfile(request,pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact/contact-profile.html', {'contact': contact})


def editContact(request,pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['full_name']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone_number']
        contact.address = request.POST['address']
        contact.save()
        return redirect('/profile/' + str(contact.id))
    return render(request, 'contact/edit.html', {'contact': contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/contact')
    return render(request, 'contact/delete.html', {'contact': contact})