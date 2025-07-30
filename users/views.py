from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import RegistrationForm
from users.models import EmailUser

class RegisterView(CreateView):
    model = EmailUser
    form_class = RegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
