import datetime

from django.http import HttpResponse
from django.views.generic import ListView

from .models import Task


def welcome(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class TaskListView(ListView):
    model = Task

    ordering = ['position']
