from django import forms
from .models import Student

class AllFieldForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Include all fields from the model
