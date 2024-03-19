from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Client
from .forms import CreateClientForm, UpdateClientForm

# Create your views here.

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients.html', {
        'clients': clients
    })
    
    
    
def create_clients(request):
    form = CreateClientForm()
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client created')
        return HttpResponseRedirect(reverse_lazy('clients'))
    return render(request, 'clients/create_clients.html', {
        'form': form
    })
    



def view_clients(request, pk):
    clients = Client.objects.get(id=pk)
    return render(request, 'clients/view_clients.html', {
        'client': clients
    })
    
    
    
def update_clients(request, pk):
    clients = Client.objects.get(id=pk)
    form = UpdateClientForm(instance=clients)
    if request.method == 'POST':
        form = UpdateClientForm(request.POST, instance=clients)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated')
        return HttpResponseRedirect(reverse_lazy('clients'))
    return render(request, 'clients/update_clients.html', {
        'form': form
    })
    
    
    
def delete_clients(request, pk):
    clients = Client.objects.get(id=pk)
    clients.delete()
    messages.success(request, 'Client deleted')
    return HttpResponseRedirect(reverse_lazy('clients'))
    
    
            
    
