from allauth.account.forms import SignupForm
from core.appvars import MANAGER


class ManagerSignupForm(SignupForm):
    def save(self, request):
        user = super(ManagerSignupForm, self).save(request)
        user.user_type = MANAGER
        user.save()
        return user
