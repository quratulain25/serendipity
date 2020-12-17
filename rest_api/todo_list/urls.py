from django.urls import include, path
from rest_framework import routers

from rest_api.todo_list import views

router = routers.DefaultRouter()
router.register(r'pages', views.PageViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('api/', include((router.urls))),
]
