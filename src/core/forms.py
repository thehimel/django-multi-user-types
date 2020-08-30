from allauth.account.forms import SignupForm
from core.appvars import (
    MANAGER, FIRST_NAME_MAX_LENGTH, LAST_NAME_MAX_LENGTH
)
from django import forms
from core.models import User


class EmployeeSignupForm(SignupForm):

    # By default email, username, password fields are loaded in the form.
    # Add these fields here and include them in the save method.
    first_name = forms.CharField(
        max_length=FIRST_NAME_MAX_LENGTH, label='First Name')
    last_name = forms.CharField(
        max_length=LAST_NAME_MAX_LENGTH, label='Last Name')

    def save(self, request):
        user = super(EmployeeSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user_type not required as default is EMPLOYEE
        user.save()
        return user


class ManagerSignupForm(SignupForm):

    first_name = forms.CharField(
        max_length=FIRST_NAME_MAX_LENGTH, label='First Name')
    last_name = forms.CharField(
        max_length=LAST_NAME_MAX_LENGTH, label='Last Name')

    def save(self, request):
        user = super(ManagerSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = MANAGER
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'gender', 'pro_pic', ]
