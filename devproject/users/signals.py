from venv import create
from django.db.models.signals import post_save, post_delete

from users.models import Profile
from django.contrib.auth.models import User

def createProfile(sender, instance, created, **kwargs):
    print('Profile Created signal Triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.firstname
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)