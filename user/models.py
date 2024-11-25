from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_super = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', 'cpf', 'phone', 'password', 'address']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name
