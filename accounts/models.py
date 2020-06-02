from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver 

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
