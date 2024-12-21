from django.contrib import admin
from .models import Store, Employee


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass