from django.urls import path
from .views import test
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(test), name='home'),
]
