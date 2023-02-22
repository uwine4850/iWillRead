from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from user.models import ProfileModel
from tinymce.models import HTMLField


class SectionModel(models.Model):
    parent_profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = HTMLField(max_length=300)
    image = models.ImageField(upload_to='sectionTitleImages/')
    tags = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('section', kwargs={'slug': self.id})

    def get_edit_url(self):
        return reverse('section_edit', kwargs={'slug': self.id})

    def __str__(self):
        return f"section - {self.name}"


@receiver(pre_save, sender=SectionModel)
def add_profile_to_section(sender, instance, *args, **kwargs):
    import inspect
    request = None
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    if request and request.user.username != 'root':
        instance.parent_profile = ProfileModel.objects.get(user=request.user)


class SubSectionModel(models.Model):
    name = models.CharField(max_length=100)
    parent_section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)

    def get_edit_url(self):
        return reverse('subsection_edit', kwargs={'slug': self.id})

    def __str__(self):
        return self.name


class PublicationModel(models.Model):
    parent_profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = HTMLField(max_length=300)
    image = models.ImageField(upload_to='publicationTitleImages/', null=True)
    category = models.ForeignKey(SubSectionModel, on_delete=models.CASCADE)
    tags = models.CharField(max_length=300)
    content = HTMLField(max_length=300, blank=True, null=True)

    def get_category_edit_url(self):
        return reverse('edit_publication_content', kwargs={'slug': self.id})

    def get_edit_url(self):
        return reverse('edit_publication', kwargs={'slug': self.id})

    def get_absolute_url(self):
        return reverse('publication', kwargs={'slug': self.id})

    def __str__(self):
        return f"{self.id} - {self.name}"


@receiver(pre_save, sender=PublicationModel)
def add_profile_to_section(sender, instance, *args, **kwargs):
    import inspect
    request = None
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    if request and request.user.username != 'root':
        instance.parent_profile = ProfileModel.objects.get(user=request.user)


class PublicationSection(models.Model):
    name = models.CharField(max_length=100)
    parent_publication = models.ForeignKey(PublicationModel, on_delete=models.CASCADE)
    content = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.name

