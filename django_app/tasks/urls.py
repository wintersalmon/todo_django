from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='home-all'),
    path('category/<title>/', views.index, name='home'),
    path('prev/', views.prev_tasks, name='prev-tasks'),
    path('task/update/status/<int:pk>', views.update_task_status, name='update-task-status'),
    path('task/update/up/<int:pk>', views.update_task_position_up, name='update-task-position-up'),
    path('task/update/down/<int:pk>', views.update_task_position_down, name='update-task-position-down'),
    path('task/delete/<int:pk>/', views.task_delete, name='task-delete'),
    # path('task/update/<int:pk>/', views.task_update, name='task-update'),
]
