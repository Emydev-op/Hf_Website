from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=15, null=True, blank=True)
    roomId = models.CharField(max_length=10, null=True, blank=True)
    department = models.CharField(max_length=40, null= True, blank=True)
    image = models.ImageField(default= 'mick.png', upload_to= 'images', blank= True)
    lga = models.CharField(max_length=40, null= True, blank=True)
    stage_origin = models.CharField(max_length=40, null= True, blank=True)
    religion = models.CharField(max_length=40, null= True, blank=True)
    reg_no = models.CharField(max_length=40, null= True, blank=True)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()