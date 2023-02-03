from django.contrib import admin
from .models import SectionModel, SubSectionModel, PublicationModel, PublicationSection


admin.site.register(SectionModel)
admin.site.register(SubSectionModel)
admin.site.register(PublicationModel)
admin.site.register(PublicationSection)
