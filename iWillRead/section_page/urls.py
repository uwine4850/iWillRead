from django.urls import path
from .views import SectionCreate, SectionDetail, SubSectionCreate, \
    PublicationCreate, get_subsection_value, PublicationDetail, SectionEdit, SubSectionEdit, \
    PublicationContentEdit, PublicationEdit, publication_content_upload_image
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('view/<int:slug>', login_required(SectionDetail.as_view()), name='section'),
    path('edit/<int:slug>', login_required(SectionEdit.as_view()), name='section_edit'),
    path('subsection/edit/<int:slug>', login_required(SubSectionEdit.as_view()), name='subsection_edit'),
    path('publication/<int:slug>', login_required(PublicationDetail.as_view()), name='publication'),
    path('publication/<int:slug>/edit', login_required(PublicationEdit.as_view()), name='edit_publication'),
    path('publication/<int:slug>/content-edit', login_required(PublicationContentEdit.as_view()),
         name='edit_publication_content'),
    path('publication/<int:slug>/upload_image', publication_content_upload_image,
         name='upload_image'),
    path('new-section', login_required(SectionCreate.as_view()), name='new_section'),
    path('new-subsection', login_required(SubSectionCreate.as_view()), name='new_subsection'),
    path('new-publication', login_required(PublicationCreate.as_view()), name='new_publication'),
    # path('new-subsection-publication', login_required(PublicationSectionCreate.as_view()), name='new_subsection_publication'),

    path('get-subsection-data', login_required(get_subsection_value), name='get_subsection_value')
]
