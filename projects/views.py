from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .forms import CreateProjectForm, UpdateProjectForm
from .models import Project
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })
    
    
    

def create_projects(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created')
        return HttpResponseRedirect(reverse_lazy('projects'))
    return render(request, 'projects/create_projects.html', {
        'form': form
    })
    
    

def view_projects(request, pk):
    projects = Project.objects.get(id=pk)
    return render(request, 'projects/view_projects.html', {
        'project': projects
    })

    
def update_projects(request, pk):
    projects = Project.objects.get(id=pk)
    form = UpdateProjectForm(instance=projects)
    if request.method == 'POST':
        form = UpdateProjectForm(request.POST, instance=projects)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated')
        return HttpResponseRedirect(reverse_lazy('projects'))
    return render(request, 'projects/update_projects.html', {
        'form': form
    })
    
    
    
def delete_projects(request, pk):
    projects = Project.objects.get(id=pk)
    projects.delete()
    messages.success(request, 'Project deleted')
    return HttpResponseRedirect(reverse_lazy('projects'))
