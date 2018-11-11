from rest_framework import serializers

from .models import Category, Task


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)

    class Meta:
        model = Category

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=32)

    class Meta:
        model = Task
        fields = ('pk', 'title', 'content', 'status', 'priority', 'position', 'created_at', 'due_date')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def validate_title(self, data):
        title = data

        try:
            validated_title = Category.objects.get(title=title)
        except Category.DoesNotExist:
            validated_title = Category.objects.create(title=title)

        return validated_title
