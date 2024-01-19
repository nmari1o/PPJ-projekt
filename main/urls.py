from django.urls import path
from . import views
from main.views import *
app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.all_tasks, name="all_tasks" ),
    path('tasks/<str:category>/', views.tasks_by_category, name='tasks_by_category'),
    path('task_input/', views.task_input, name='task_input'),

    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

    path('task_completed/<int:task_id>/', views.task_completed, name='task_completed'),
]