from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import ProjectSerilizer
from projects.models import Project

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET' : '/api/projects/'},
        {'GET' : '/api/projects/id'},
        {'POST' : '/api/projects/id/vote'},

        {'POST' : '/api/users/token'},
        {'POST' : '/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializedProjects = ProjectSerilizer(projects, many=True)
    return Response(serializedProjects.data)


@api_view(['GET'])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializedProjects = ProjectSerilizer(projects, many=False)
    return Response(serializedProjects.data)