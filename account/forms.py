from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# a class for users to register and create account
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match!')
        return cd['password2']


# these classes are for users to edit their profile
class UserEditForm(forms.ModelForm):
    """This is for users to change their default data"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """This is for user to change DB and photos"""

    class Meta:
        model = Profile
        fields = ('gender', 'phone', 'user_type', 'address', 'town', 'post_code',
                  'country', 'longitude', 'latitude')
