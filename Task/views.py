from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TaskSerializer
# changes added
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Task

class TaskView(viewsets.ModelViewSet):
    serializer_class=TaskSerializer
    queryset=Task.objects.all()