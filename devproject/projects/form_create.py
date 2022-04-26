from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import Project
from django.forms import ModelForm
from django import forms

class CreateProject(ModelForm):
    class Meta:
        model = Project
        #fields = '__all__' # this creates all the fields of our model
        fields = ['title', 'description', 'featured_image', 'demo_link' , 'source_link', 'tags']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs) -> None:
        # this function overrides the initial load of ADD Project Page. 
        super(CreateProject, self).__init__(*args, **kwargs)

        # By these lines we set the attributes of required Field in our form.
        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Description About Your Project'})
        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Title'})
        # self.fields['featured_image'].widget.attrs.update({'class' : 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Paste Your Demo Link'})
        # self.fields['source_link'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Paste Your Source Link'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input', 'placeholder' : 'Add ' + name})