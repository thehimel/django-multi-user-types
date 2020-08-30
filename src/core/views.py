# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import TemplateView
from allauth.account.views import SignupView

from .forms import EmployeeSignupForm, ManagerSignupForm
from .forms import UserUpdateForm


class HomeView(TemplateView):

    template_name = "core/home.html"


# Employee Signup View
class EmployeeSignupView(SignupView):

    template_name = 'auth/signup.html'  # Custom template is mandatory
    form_class = EmployeeSignupForm
    redirect_field_name = 'next'  # Important to redirect user if has next url

    # This is mandatory and copy-pasted
    def get_context_data(self, **kwargs):
        ret = super(EmployeeSignupView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


# Manager Signup View
class ManagerSignupView(SignupView):

    template_name = 'auth/signup.html'
    form_class = ManagerSignupForm
    redirect_field_name = 'next'  # Important to redirect user if has next url

    def get_context_data(self, **kwargs):
        ret = super(ManagerSignupView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


# Common Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES,
                              instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('core:profile')

    # If it's not POST, it's GET. Thus generate the form.
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'auth/profile.html', context)
