from django.forms import ModelForm, CharField

from .models import Task, Category


class TaskForm(ModelForm):
    title = CharField(required=True)

    class Meta:
        model = Task
        fields = ['title', 'status', 'content', 'priority', 'position', 'due_date']

    def clean_title(self):
        data = self.cleaned_data['title']

        try:
            data = Category.objects.get(title=data)
        except Category.DoesNotExist:
            data = Category.objects.create(title=data)

        return data
