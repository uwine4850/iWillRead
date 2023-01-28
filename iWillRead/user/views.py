from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import ProfileModel
from django.http.request import HttpRequest
from django.db.models import Model
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin


class ProfileEditPermissionMixin(PermissionRequiredMixin):
	def has_permission(self):
		return self.get_object().user.id == self.request.user.id


class ProfileEdit(ProfileEditPermissionMixin, DetailView):
	model = ProfileModel
	context_object_name = 'profile'
	template_name = 'profile/update_profile.html'
	slug_field = 'id'

	def post(self, request: HttpRequest, *args, **kwargs):
		username = request.POST.get('username')
		image = request.FILES.get('image')

		current_user: Model = request.user
		current_profile = ProfileModel.objects.get(user=current_user)

		if username:
			User.objects.filter(id=current_user.id).update(username=username)
		if image:
			current_profile.image = image
			current_profile.save()
		return redirect('home')
