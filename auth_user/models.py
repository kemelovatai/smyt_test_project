from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from utils.managers import UserManager
from utils.models import BaseModel


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_email_recipient = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    objects = UserManager()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.full_name)
