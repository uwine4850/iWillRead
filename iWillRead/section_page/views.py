from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from .models import SectionModel, SubSectionModel, PublicationModel, PublicationSection
from django.http import JsonResponse, Http404
from django.contrib.auth.mixins import PermissionRequiredMixin


class PublicationCreatePermissionMixin(PermissionRequiredMixin):
	def has_permission(self):
		s = SectionModel.objects.get(id=int(self.request.GET.get('parentsection_id')))
		if s.subsectionmodel_set.count():
			return True
		else:
			return False


class SectionSubsectionCreatePermissionMixin(PermissionRequiredMixin):
	def has_permission(self):
		s = SectionModel.objects.get(id=int(self.request.GET.get('parentsection_id')))
		if s.subsectionmodel_set.count():
			return True
		else:
			return False


class SubSectionEditPermissionMixin(PermissionRequiredMixin):
	def has_permission(self):
		s = self.get_object()
		if s.parent_section.parent_profile == self.request.user.profilemodel:
			return True
		else:
			return False


class SectionEditPermissionMixin(PermissionRequiredMixin):
	def has_permission(self):
		s = self.get_object()
		if s.parent_profile == self.request.user.profilemodel:
			return True
		else:
			return False


class SectionCreate(CreateView):
	model = SectionModel
	template_name = 'section/new_section.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse('section', kwargs={'slug': self.object.id})


class SectionDetail(DetailView):
	model = SectionModel
	context_object_name = 'section'
	template_name = 'section/section.html'
	slug_field = 'id'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['default_ss'] = self.object.subsectionmodel_set.first()
		if context['default_ss']:
			context['default_ss_values'] = context['default_ss'].publicationmodel_set.all()
		context['tags'] = ', '.join(['#' + i.strip(' ') for i in self.object.tags.split(',')])
		return context

	def post(self, request, *args, **kwargs):
		if 'delete_section_id' in request.POST:
			section = SectionModel.objects.get(id=int(request.POST.get('delete_section_id')))
			if section.parent_profile == request.user.profilemodel:
				section.delete()
		if 'delete_subsection_id' in request.POST:
			subsection = SubSectionModel.objects.get(id=int(request.POST.get('delete_subsection_id')))
			if subsection.parent_section.parent_profile == request.user.profilemodel:
				subsection.delete()
		return redirect('home')


class SectionEdit(SectionEditPermissionMixin, UpdateView):
	model = SectionModel
	context_object_name = 'section'
	template_name = 'section/new_section.html'
	fields = '__all__'
	slug_field = 'id'


def get_subsection_value(request):
	count = request.GET.get('count')
	sub_id = request.GET.get('sub_id')
	sub_objects = list(SubSectionModel.objects.get(id=int(sub_id)).publicationmodel_set.all()[:int(count)].values())
	return JsonResponse({'sub_objects': sub_objects})


class SubSectionCreate(CreateView):
	model = SubSectionModel
	template_name = 'section/new_subsection.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse('section', kwargs={'slug': self.request.GET.get('parentsection_id')})

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['section'] = SectionModel.objects.get(id=int(self.request.GET.get('parentsection_id')))
		return context


class SubSectionEdit(SubSectionEditPermissionMixin, UpdateView):
	model = SubSectionModel
	template_name = 'section/new_subsection.html'
	fields = '__all__'
	slug_field = 'id'

	def get_success_url(self):
		return reverse('section', kwargs={'slug': self.request.GET.get('parentsection_id')})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['section'] = SectionModel.objects.get(id=int(self.request.GET.get('parentsection_id')))
		return context


class PublicationCreate(PublicationCreatePermissionMixin, CreateView):
	model = PublicationModel
	template_name = 'section/new_publication.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse('section', kwargs={'slug': self.request.GET.get('parentsection_id')})

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['current_section'] = SectionModel.objects.get(id=int(self.request.GET.get('parentsection_id')))
		return context


class PublicationDetail(DetailView):
	model = PublicationModel
	context_object_name = 'publication'
	template_name = 'section/publication.html'
	slug_field = 'id'


class PublicationSectionCreate(CreateView):
	model = PublicationSection
	template_name = 'section/new_subsection_publication.html'
	fields = '__all__'

	def get_success_url(self):
		return PublicationModel.objects.get(id=int(self.request.GET.get('publication_id'))).get_absolute_url()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['publication'] = PublicationModel.objects.get(id=int(self.request.GET.get('publication_id')))
		return context


def section(request):
	return render(request, 'section/section.html')


def publication(request):
	return render(request, 'section/publication.html')


def new_section(request):
	return render(request, 'section/new_section.html')


def new_publication(request):
	return render(request, 'section/new_publication.html')


def new_subsection(request):
	return render(request, 'section/new_subsection.html')


def new_subsection_publication(request):
	return render(request, 'section/new_subsection_publication.html')