from django.urls import path
from .views import section, publication, new_section, new_subsection, new_subsection_publication, new_publication


urlpatterns = [
	path('', section, name='section'),
	path('publication', publication, name='publication'),
	path('new-section', new_section, name='new_section'),
	path('new-subsection', new_subsection, name='new_subsection'),
	path('new-publication', new_publication, name='new_publication'),
	path('new-subsection-publication', new_subsection_publication, name='new_subsection_publication'),
]