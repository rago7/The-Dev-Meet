from operator import truediv
from turtle import title
from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    demo_link = models.CharField(max_length = 2000, null = True, blank = True)
    source_link = models.CharField(max_length = 2000, null = True, blank = True)
    created = models.DateField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    tags = models.ManyToManyField('Tag', blank = True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    body = models.TextField(null = True, blank = True)
    created = models.DateField(auto_now_add = True)
    value = models.CharField(max_length = 200, choices = VOTE_TYPE)

    def __str__(self) -> str:
        return self.value

class Tag(models.Model):
    created = models.DateField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    name = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.name