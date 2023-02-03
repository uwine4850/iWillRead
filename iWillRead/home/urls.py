from django.urls import path
from .views import SectionView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(SectionView.as_view()), name='home'),
]
