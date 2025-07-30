from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import RegistrationForm
from users.models import EmailUser
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    model = EmailUser
    form_class = RegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

class UserLoginView(LoginView):
    template_name = "users/login.html"
