from django import forms
from .models import PublicationModel


class PublicationContentEditForm(forms.ModelForm):
    class Meta:
        model = PublicationModel
        fields = ('content',)


class PublicationEditForm(forms.ModelForm):
    class Meta:
        model = PublicationModel
        fields = ('name', 'description', 'image', 'category', 'tags')
