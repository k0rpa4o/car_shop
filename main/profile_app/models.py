from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null= True)
    designation = models.CharField(max_length=100, null= True)
    mobile_number = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(null=True, upload_to='static/images/' )
    profile_summary = models.TextField(max_length=300, null= True)
    city = models.CharField(max_length=100, null= True)
    state = models.CharField(max_length=100, null= True)
    country = models.CharField(max_length=100, null= True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()