from django import forms
from .models import Post,Profile, Business

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'name', 'email', 'location', 'occupant_id']