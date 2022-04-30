from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from projects.form_create import CreateProject
from django.contrib.auth.decorators import login_required

from projects.models import Project


# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'list' : projects}
    # return HttpResponse('Here are the projects')
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    isFound = False
    projectObj = Project.objects.get(id = pk)
    if(projectObj):
        isFound = True
        tags = projectObj.tags.all()
    
    context = {'key' : pk, 'item' : projectObj, 'isFound': isFound, 'tags' : tags}
    # return HttpResponse('single project' + ' ' + str(pk) )
    return render(request, 'projects/single-projects.html', context)

@login_required(login_url='login')
def createProject(request):
    form = CreateProject()
    if request.method == 'POST':
        form = CreateProject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = CreateProject(instance=project)
    if request.method == 'POST':
        form = CreateProject(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html', context)
