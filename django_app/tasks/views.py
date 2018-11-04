from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import TaskForm
from .models import Task, Category


def index(request, title=None):
    context = {
        'task_form': TaskForm(),
        'category_list': Category.objects.all()
    }
    if title is None:
        context.update({'task_list': Task.objects.all().order_by('title', 'position')})
    else:
        context.update({'task_list': Task.objects.filter(title=title).order_by('title', 'position')})

    return render(request, 'tasks/index.html', context)


def task_create(request):
    return HttpResponse('Task create')


def task_update(request, pk):
    return HttpResponse('Task update {}'.format(pk))


def task_delete(request, pk):
    return HttpResponse('Task delete {}'.format(pk))


class TaskListView(ListView):
    model = Task

    ordering = ['title', 'position']


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_new.html'
    success_url = reverse_lazy('home')
