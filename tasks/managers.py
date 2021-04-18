# -
from django.db import models


class TaskManager(models.Manager):

    def tasks_by_owner(self, user):
        return self.filter(
            owner=user
        )
