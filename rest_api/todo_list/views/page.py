from rest_framework import viewsets

from todo_list.models import Page
from rest_api.todo_list.serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
