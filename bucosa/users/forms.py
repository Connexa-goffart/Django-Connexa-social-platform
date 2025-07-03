from .models import user_profile, GroupProfile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import Group

class profileForm(ModelForm):
    class Meta:
        model = user_profile
        exclude = ['user']

class GroupCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Group
        fields = ['name', 'description']

class GroupProfileForm(forms.ModelForm):
    class Meta:
        model = GroupProfile
        fields = ['profile_image']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = user_profile
        fields = ['bio', 'profile_image', 'cover_image', 'website', 'location']