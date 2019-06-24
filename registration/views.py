from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import IITJUser
from .forms import RegistrationForm
from django.urls import reverse
# Create your views here.
@login_required
def homepage(request):
	print(request.user.is_active)
	return render(request,'detail.html')


class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('home')