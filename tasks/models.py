from django.db import models
from django.conf import settings

from .managers import TaskManager


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField();
    is_completed = models.BooleanField();
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    deadline = models.DateField(null=True, blank=True)

    objects = TaskManager()

    def __str__(self):
        return (
            f"{self.title} - {self.owner.username if self.owner else ''}"
        )
