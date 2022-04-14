from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'E-commerce-Website',
        'description': 'Fully Functional E-commerce Website'
    },
    {
        'id': '2',
        'title': 'Portfilo-Website',
        'description': 'This was a project to build out my portfilo'
    },
    {
        'id': '3',
        'title': 'Social Networking Website',
        'description': 'Awesome social networking project i\'m working on'
    }
]

def projects(request):
    msg = 'you are in projects page'
    number = 19
    context = {'message' : msg , 'number' : number, 'list' : projectsList}
    # return HttpResponse('Here are the projects')
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    msg = 'you are in single-project page'
    number = 20
    isFound = False
    for item in projectsList :
        if item['id'] == pk :
            isFound = True
    context = {'message' : msg , 'number' : number, 'key' : pk, 'list' : projectsList, 'isFound': isFound}
    # return HttpResponse('single project' + ' ' + str(pk) )
    return render(request, 'projects/single-projects.html', context)

