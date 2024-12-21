from django.urls import path
from .views import UserView, UserDetailView, AuthUserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", UserView.as_view(), name = "users"),
    path("detail/", AuthUserDetailView.as_view(), name = "user-detail"),
    path("<int:pk>/", UserDetailView.as_view(), name = "user"),
    path("login/", TokenObtainPairView.as_view(), name = "user-login"),
]