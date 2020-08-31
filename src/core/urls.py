from django.urls import path
from .views import HomeView

app_name = 'core'

urlpatterns = [
    # url: '', name = core:home
    path('', HomeView.as_view(), name='home'),
]
