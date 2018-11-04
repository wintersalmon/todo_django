from django.urls import path

from . import views

app_name = 'tasks'


urlpatterns = [
    path('', views.index, name='home'),
    # path('<slug:title>/', views.index, name='home'),
    # path('task/create/', views.TaskCreateView.as_view(), name='task-create'),
    # path('task/delete/<int:pk>/', views.task_delete, name='task-delete'),
    # path('task/update/<int:pk>/', views.task_update, name='task-update'),
]
