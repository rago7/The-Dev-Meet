from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name'
        }

    def __init__(self, *args, **kwargs) -> None:
        # this function overrides the initial load of ADD Project Page. 
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # By these lines we set the attributes of required Field in our form.
        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Description About Your Project'})
        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Title'})
        # self.fields['featured_image'].widget.attrs.update({'class' : 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Paste Your Demo Link'})
        # self.fields['source_link'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Paste Your Source Link'})

        for name, field in self.fields.items():
            if name != 'password1' and name != 'password2':
                field.widget.attrs.update({'class' : 'input', 'placeholder' : 'Add ' + name})
            else:
                field.widget.attrs.update({'class' : 'input', 'placeholder' : ('Password' if name == 'password1' else 'Confirm Password')})

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'bio', 'short_intro', 'email', 'profile_image', 'social_github', 'social_linkedIn', 'social_youtube', 'location']

    def __init__(self, *args, **kwargs) -> None:
        # this function overrides the initial load of ADD Project Page. 
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        # By these lines we set the attributes of required Field in our form.
        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Description About Your Project'})
        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Add Title'})
        # self.fields['featured_image'].widget.attrs.update({'class' : 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Paste Your Demo Link'})
        # self.fields['source_link'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Paste Your Source Link'})

        for name, field in self.fields.items():
            if name != 'password1' and name != 'password2':
                field.widget.attrs.update({'class' : 'input', 'placeholder' : 'Add ' + name})
            else:
                field.widget.attrs.update({'class' : 'input', 'placeholder' : ('Password' if name == 'password1' else 'Confirm Password')})

