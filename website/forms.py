from django import forms

from .models import Application
# import the built in form AND model
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'