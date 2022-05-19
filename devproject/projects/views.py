from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from projects.form_create import CreateProject
from django.contrib.auth.decorators import login_required

from projects.models import Project
from projects.utils import searchProject


# Create your views here.

def projects(request):
    projects, search_query = searchProject(request)
    context = {'list' : projects, 'search':search_query}
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
    profile = request.user.profile
    form = CreateProject()
    if request.method == 'POST':
        form = CreateProject(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = CreateProject(instance=project)
    if request.method == 'POST':
        form = CreateProject(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('projects')
    context = {'object':project, 'back':'projects', 'type':'Project'}
    return render(request, 'delete_template.html', context)
