from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from serendipity import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
] + static(settings.STATIC_URL)
