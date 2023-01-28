from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.user}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.id})

    @staticmethod
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, *args, **kwargs):
        if created and instance.username != 'root':
            ProfileModel.objects.create(user=instance)

