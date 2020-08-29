# from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import SignupView
from .forms import ManagerSignupForm


class HomeView(TemplateView):
    template_name = "core/home.html"


class ManagerSignupView(SignupView):
    template_name = 'core/auth/signup.html'
    form_class = ManagerSignupForm
    redirect_field_name = 'next'  # Important to redirect user if has next url

    def get_context_data(self, **kwargs):
        ret = super(ManagerSignupView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret
