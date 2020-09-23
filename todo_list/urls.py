from django.urls import path
from django.conf.urls.static import static

from serendipity import settings
from todo_list import views

app_name = 'todo_list'
urlpatterns = [path('', views.dashboard_view, name='dashboard'),
               path('edit_page/<int:pk>', views.edit_page_view, name='edit_page'),
               path('delete_page/<int:pk>', views.delete_page_view, name='delete_page'),
               path('create_page', views.create_page_view, name='create_page'),
               path('list_page', views.list_page_view, name='list_page'),

               path('edit_task/<int:pk>', views.edit_task_view, name='edit_task'),
               path('delete_task/<int:pk>', views.delete_task_view, name='delete_task'),
               path('<int:page_id>/create_task', views.create_task_view, name='create_task'),
               ] + static(settings.STATIC_URL)
