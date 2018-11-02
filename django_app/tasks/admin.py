from django.contrib import admin

from .forms import TaskForm
from .models import Category, Task


class TaskAdmin(admin.ModelAdmin):
    form = TaskForm


admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
