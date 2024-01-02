from django import forms
from . import models
class AddBrandform(forms.ModelForm):
    model = models.BrandModel
    fields = '__all__'