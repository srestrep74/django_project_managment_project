# myapp/forms.py
from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(label='name', max_length=200, required=True)
    description = forms.CharField(label='description', widget=forms.Textarea, required=True)
    start_date = forms.DateField(label='start_date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    end_date = forms.DateField(label='end_date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
