from django import forms


# a class to invite members
class CircleInviteForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=30)
    to = forms.EmailField(max_length=30)
    url = forms.CharField(widget=forms.HiddenInput(attrs={'value': "{% url 'circle:join' slug=circle.slug %}"}))
