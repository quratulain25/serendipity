from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from serendipity import settings

app_urls = [
    path('', include('todo_list.urls')),
    path('', include('rest_api.todo_list.urls')),
]

main_urls = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = app_urls + main_urls + static(settings.STATIC_URL)
