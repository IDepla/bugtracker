from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from typing import List



class UserManager(BaseUserManager):
    """Define a model manager for User model with optional username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
class User(AbstractUser):
    """System user"""

    objects: BaseUserManager = UserManager()

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
