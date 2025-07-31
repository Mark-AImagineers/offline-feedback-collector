from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import RegistrationForm
from users.models import EmailUser
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class RegisterView(CreateView):
    model = EmailUser
    form_class = RegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

class UserLoginView(LoginView):
    template_name = "users/login.html"

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "users/dashboard.html"