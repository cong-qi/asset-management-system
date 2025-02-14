from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    wechat_department_id = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="users",
    )
    job_title = models.CharField(max_length=100, blank=True)
    wechat_user_id = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.username
