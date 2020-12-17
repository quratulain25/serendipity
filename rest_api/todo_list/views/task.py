from rest_framework import viewsets

from todo_list.models import Task
from rest_api.todo_list.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
