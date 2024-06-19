# myapp/forms.py
from django import forms

class ProjectForm(forms.Form):

    name = forms.CharField(label='name', max_length=200, required=True)
    description = forms.CharField(label='description', widget=forms.Textarea, required=True)
    start_date = forms.DateField(label='start_date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    end_date = forms.DateField(label='end_date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)


    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("End date must be after start date.")

        return cleaned_data