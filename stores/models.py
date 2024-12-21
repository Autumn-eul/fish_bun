from django.db import models

from common.models import BaseModel
from users.models import User


# Create your models here.
class Store(BaseModel):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"STORE: {self.name}"

    class Meta:
        db_table = "stores"
        verbose_name = "Store"
        verbose_name_plural = "Stores"
        ordering = ["name"]
        indexes = [models.Index(fields=["name"], name="store_name_idx")]

    def active_store(self):
        return self.objects.filter(is_active = True)


class Employee(BaseModel):
    code = models.PositiveIntegerField(unique=True)
    type = models.CharField(
        max_length=8, choices=[("STAFF", "Staff"), ("MANAGER", "Manager")]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"CODE {self.code}: {self.user.first_name} at {self.store.name}"

    class Meta:
        db_table = "employees"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["store", "type", "code"]
        constraints = [
            models.UniqueConstraint(fields=["code"], name="unique_employee_code"),
        ]