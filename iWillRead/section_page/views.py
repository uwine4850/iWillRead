from django.shortcuts import render


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