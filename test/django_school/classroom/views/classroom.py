from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_foodonator:
            return redirect('foodonators:orders')
        else:
            return redirect('foodrivers:pickup_list')
    return render(request, 'classroom/home.html')
