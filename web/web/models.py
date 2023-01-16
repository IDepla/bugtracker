from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import List


class User(AbstractUser):
    """System user"""

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS: List[str] = []

    def __str__(self):
        return self.email


class Bug(models.Model):
    """Represents a bug"""

    class BugStatus(models.TextChoices):
        """Bug statuses"""

        OPEN = "O", "Open"
        CLOSE = "C", "Closed"

    title = models.TextField()

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        User,
        related_name="bugs_created",
        on_delete=models.DO_NOTHING,
    )

    status = models.CharField(
        max_length=1,
        choices=BugStatus.choices,
        default=BugStatus.OPEN,
    )

    closed_at = models.DateTimeField(null=True)
    closed_by = models.ForeignKey(
        User, related_name="bugs_closed", on_delete=models.DO_NOTHING
    )

    assigned_to = models.ManyToManyField(
        User,
        related_name="bugs_assigned",
    )
