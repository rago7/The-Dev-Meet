from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from projects.form_create import CreateProject, CreateReview
from django.contrib.auth.decorators import login_required

from projects.models import Project
from projects.utils import paginateProjects, searchProject

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginateProjects(request, 1, projects)

    context = {'list':projects, 'search':search_query, 'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    isFound = False
    review_form = CreateReview()
    projectObj = Project.objects.get(id = pk)
    if(projectObj):
        isFound = True
        tags = projectObj.tags.all()
    if request.method == 'POST':
        form = CreateReview(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = projectObj
        review.save()
        projectObj.updateVotes
        messages.success(request, 'Review Submitted !')
        return redirect('project', pk=projectObj.id)
    
    context = {'key' : pk, 'item' : projectObj, 'isFound': isFound, 'tags' : tags, 'review_form' : review_form}
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
