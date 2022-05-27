from email.policy import default
from operator import truediv
from pickle import TRUE
from turtle import title
from typing import OrderedDict
from django.db import models
import uuid

from users.models import Profile

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    demo_link = models.CharField(max_length = 2000, null = True, blank = True)
    source_link = models.CharField(max_length = 2000, null = True, blank = True)
    featured_image = models.ImageField(null = True, blank = True,  default = 'default.jpg' )
    created = models.DateField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    tags = models.ManyToManyField('Tag', blank = True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']

    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def updateVotes(self):
        reviews = self.review_set.all()
        totalVotes = reviews.count()
        upVotes = reviews.filter(value='up').count()
        ratio = (upVotes/totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=TRUE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    body = models.TextField(null = True, blank = True)
    created = models.DateField(auto_now_add = True)
    value = models.CharField(max_length = 200, choices = VOTE_TYPE)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self) -> str:
        return self.value

class Tag(models.Model):
    created = models.DateField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    name = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.name