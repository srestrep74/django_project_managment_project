# myapp/forms.py
from django import forms
from .choices import STATUS_CHOICES

class TaskForm(forms.Form):
    name = forms.CharField(label='name', max_length=200, required=True)
    description = forms.CharField(label='description', widget=forms.Textarea, required=True)
    status = forms.ChoiceField(label='status', choices=STATUS_CHOICES, required=True)