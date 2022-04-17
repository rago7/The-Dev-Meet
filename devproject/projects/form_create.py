from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import Project
from django.forms import ModelForm

class CreateProject(ModelForm):
    class Meta:
        model = Project
        #fields = '__all__' # this creates all the fields of our model
        fields = ['title', 'description', 'demo_link' , 'source_link', 'tags']