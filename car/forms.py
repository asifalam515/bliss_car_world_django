from django import forms
from . import models
class AddCarForm(forms.ModelForm):
    model = models.CarModel
    fields = '__all__'