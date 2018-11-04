from django.urls import path

from . import api_views as views

app_name = 'api'

urlpatterns = [
    path('task-list/', views.TaskList.as_view(), name='task-list-all'),
    path('task-list/<slug:title>/', views.TaskList.as_view(), name='task-list'),

    path('task/create', views.TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task'),

    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<slug:title>/', views.CategoryRetrieveUpdateDestroy.as_view(), name='category'),
]
