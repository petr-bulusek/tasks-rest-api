from rest_framework import serializers
from .models import Task


class TaskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'label', 'completed', 'sub_tasks')


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('label', )


class TaskEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('label', 'completed')
        extra_kwargs = {'label': {'required': False},
                        'completed': {'required': False}}
