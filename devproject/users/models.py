from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    created = models.DateField(auto_now_add = True)
    name = models.CharField(null=True, blank=True, max_length=200)
    username = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True, blank=True, max_length=500)
    short_intro = models.TextField(null=True, blank=True, max_length=200)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='profiles/')
    social_github = models.CharField(null=True, blank=True, max_length=200)
    social_linkedIn = models.CharField(null=True, blank=True, max_length=200)
    social_youtube = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self) -> str:
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    created = models.DateField(auto_now_add = True)
    name = models.CharField(null=True, blank=True, max_length=200)
    description = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self) -> str:
        return str(self.name)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(max_length=200, null=True)
    isRead = models.BooleanField(default=False, null=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    created = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return str(self.subject)

    class Meta:
        ordering = ['-isRead', '-created']
