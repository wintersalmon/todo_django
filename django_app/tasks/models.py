from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save

DEFAULT_CATEGORY = 'default'

STATUS_CODE = (
    ('A', 'added'),
    ('O', 'completed'),
    ('D', 'deleted'),
)


class Category(models.Model):
    title = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return 'Category({})'.format(self.title)

    def next_max_position(self):
        return len(self.task_set.all())

    def inc_all_positions(self, begin, end=None):
        if end is None:
            self.task_set.filter(position__gte=begin).update(position=F('position') + 1)
        else:
            self.task_set.filter(position__gte=begin, position__lte=end).update(position=F('position') + 1)

    def dec_all_positions(self, begin, end=None):
        if end is None:
            self.task_set.filter(position__gte=begin).update(position=F('position') - 1)
        else:
            self.task_set.filter(position__gte=begin, position__lte=end).update(position=F('position') - 1)


class Task(models.Model):
    title = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CODE, default='A')
    priority = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=None, null=True, blank=True)

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        max_position = instance.title.next_max_position()

        if instance._state.adding:  # this is an insert
            if instance.position >= max_position:
                instance.position = max_position
            else:
                instance.title.inc_all_positions(instance.position)

        else:  # this is an update
            prev_pos = Task.objects.get(pk=instance.pk).position

            if instance.position >= max_position:
                instance.position = max_position - 1
            next_pos = instance.position

            if next_pos < prev_pos:
                instance.title.inc_all_positions(next_pos, prev_pos - 1)
            elif next_pos > prev_pos:
                instance.title.dec_all_positions(prev_pos + 1, next_pos)

    def __str__(self):
        if self.due_date:
            return '[{title}][{position}] {content}/{due}'.format(
                title=self.title.title,
                content=self.content,
                position=self.position,
                due=self.due_date.strftime("%Y-%m-%d %H:%M"))
        else:
            return '[{title}][{position}] {content}'.format(
                title=self.title.title,
                content=self.content,
                position=self.position)


pre_save.connect(Task.pre_save, Task, dispatch_uid="todo_django.tasks.models.Task")
