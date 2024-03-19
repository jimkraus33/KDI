from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .forms import  CreateContactForm, UpdateContactForm
from .models import Contact
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts.html', {
        'contacts': contacts
    })
    
    
    
def create_contacts(request):
    form = CreateContactForm()
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact created')
        return HttpResponseRedirect(reverse_lazy('contacts'))
    return render(request, 'contacts/create_contacts.html', {
        'form': form
    })
    
    
    
def view_contacts(request, pk):
    contacts = Contact.objects.get(id=pk)
    return render(request, 'contacts/view_contacts.html', {
        'contact': contacts
    })
    
    
    
    
def update_contacts(request, pk):
    contacts = Contact.objects.get(id=pk)
    form = UpdateContactForm(instance=contacts)
    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated')
        return HttpResponseRedirect(reverse_lazy('contacts'))
    return render(request, 'contacts/update_contacts.html', {
        'form': form
    })
    
    
    
def delete_contacts(request, pk):
    contacts = Contact.objects.get(id=pk)
    contacts.delete()
    messages.success(request, 'Contact deleted')
    return HttpResponseRedirect(reverse_lazy('contacts'))
