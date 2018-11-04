from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import TaskForm
from .models import Task, Category


def index(request, title=None):
    context = {
        'category_list': Category.objects.all()
    }
    if title is None:
        context.update({'task_list': Task.objects.all().order_by('title', 'position')})
    else:
        context.update({'task_list': Task.objects.filter(title=title).order_by('title', 'position')})

    return render(request, 'tasks/index.html', context)


def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.status == 'A':
        task.status = 'O'
    else:
        task.status = 'A'
    task.save()
    prev_url = request.META.get('HTTP_REFERER')
    if prev_url:
        return redirect(prev_url)
    else:
        return request('/')


def update_task_position_up(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.position > 0:
        task.position -= 1
    task.save()
    prev_url = request.META.get('HTTP_REFERER')
    if prev_url:
        return redirect(prev_url)
    else:
        return request('/')


def update_task_position_down(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.position += 1
    task.save()
    prev_url = request.META.get('HTTP_REFERER')
    if prev_url:
        return redirect(prev_url)
    else:
        return request('/')


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    category = task.title
    task.delete()

    if category.next_max_position() == 0:
        return request('/')

    prev_url = request.META.get('HTTP_REFERER')
    if prev_url:
        return redirect(prev_url)
    else:
        return request('/')


class TaskListView(ListView):
    model = Task

    ordering = ['title', 'position']


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_new.html'
    success_url = reverse_lazy('home')
