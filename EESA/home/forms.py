from .models import SlideImage
from django import forms

class SlideImageUpload(forms.ModelForm):
    class Meta:
        fields = '__all__'