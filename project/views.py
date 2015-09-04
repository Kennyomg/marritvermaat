from django.shortcuts import render
from models import Project
from rest_framework import generics
from serializers import ProjectSerializer

# Create your views here.
def all_projects(request):
    return render(request, 'project/all_projects.html')

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'project/project.html', {'project':project})