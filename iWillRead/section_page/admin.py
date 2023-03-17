from django.contrib import admin
from .models import SectionModel, SubSectionModel, PublicationModel


admin.site.register(SectionModel)
admin.site.register(SubSectionModel)
admin.site.register(PublicationModel)
