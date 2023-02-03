from django.urls import path
from .views import ProfileEdit
from django.contrib.auth.decorators import login_required


urlpatterns = [
	path('update/<slug:slug>/', login_required(ProfileEdit.as_view()), name='profile')
]
