from django.urls import path
from .views import HomeView
from .views import profile

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', profile, name='profile'),
]
