from django.urls import path
from users.views import RegisterView, UserLoginView, DashboardView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]