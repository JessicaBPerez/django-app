from django import forms
from .models import School, Professor

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'image_url')

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('name', 'image_url', 'subject', 'school')