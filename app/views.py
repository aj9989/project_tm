from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from datetime import datetime
from celery import Celery



#Task Lisk Views to create api with DateTime and url as parameter.

class Index(ListView):
    model = Task
    template_name = 'index.html'


class TaskListView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    localtime = datetime.now()
    tasktime = Task.DateTime()
    print(tasktime)









