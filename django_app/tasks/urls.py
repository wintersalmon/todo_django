from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('tasks', views.TaskListView.as_view(), name='tasks')
]
