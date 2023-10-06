from django.db import models
from .choices import STATUS_CHOICES, PRIORITY_CHOICES

class Task(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

