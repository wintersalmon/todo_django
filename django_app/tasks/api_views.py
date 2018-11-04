from rest_framework import generics

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category


class TaskCreate(generics.CreateAPIView):
    serializer_class = TaskSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    ordering_fields = ('title', 'position')

    def get_queryset(self):
        try:
            title = self.kwargs['title']
        except KeyError:
            title = None

        if title is None:
            return Task.objects.all()
        else:
            return Task.objects.filter(title=title)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task
