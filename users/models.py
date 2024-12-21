from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from common.models import BaseModel


class UserManager(BaseUserManager):
    def active_user(self):
        return self.filter(is_active=True)

    def active_staff(self):
        return self.filter(is_staff=True, is_active=True)

    def withdraw_user(self):
        return self.filter(is_active=False, is_staff=False)

    def withdraw_staff(self):
        return self.filter(is_staff=True, is_active=False)
        
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
    # user 정보를 email 과 password 만 받아오고 싶으면 위의 create_superuser 함수를 추가해야함

class User(AbstractBaseUser, BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=50, null=True)
    gender = models.CharField(
        max_length=6, choices=[("MALE", "Male"), ("FEMALE", "Female")]
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
        
    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return False
    
    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return False

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"