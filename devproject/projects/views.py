from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from projects.form_create import CreateProject

from projects.models import Project


# Create your views here.

def projects(request):
    msg = 'you are in projects page'
    number = 19
    projects = Project.objects.all()
    context = {'list' : projects}
    # return HttpResponse('Here are the projects')
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    msg = 'you are in single-project page'
    number = 20
    isFound = False
    projectObj = Project.objects.get(id = pk)
    if(projectObj):
        isFound = True
        tags = projectObj.tags.all()
    
    context = {'key' : pk, 'item' : projectObj, 'isFound': isFound, 'tags' : tags}
    # return HttpResponse('single project' + ' ' + str(pk) )
    return render(request, 'projects/single-projects.html', context)

def createProject(request):
    form = CreateProject()
    if request.method == 'POST':
        form = CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = CreateProject(instance=project)
    if request.method == 'POST':
        form = CreateProject(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html', context)