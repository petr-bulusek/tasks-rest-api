from django.db import models


class Task(models.Model):
    label = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    parent = models.ForeignKey('Task', on_delete=models.CASCADE,
                               related_name='sub_tasks', null=True)
