from django.urls import path
from .views import StoreView, StoreDetailView, EmployeeView, EmployeeDetailView


urlpatterns = [
    path("stores/", StoreView.as_view(), name = "stores"),
    path("stores/<int:pk>/", StoreDetailView.as_view(), name = "store"),
    path("employees/", EmployeeView.as_view, name = "employees"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name = "employee")
]