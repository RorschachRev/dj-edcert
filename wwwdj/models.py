from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# User Model Extension
# TODO:
# Add fields relevant to a user's Profile
# 	(user_type, area_of_study, phone_number, etc.)
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name_first = models.CharField(max_length=30, null=True, blank=True, verbose_name='First Name')
	name_last = models.CharField(max_length=30, null=True, blank=True, verbose_name='Last Name')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
