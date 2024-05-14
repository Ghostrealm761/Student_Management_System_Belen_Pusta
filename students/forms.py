from dataclasses import fields
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {'first_name','last_name','course','grade','age'}
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'course': 'Course',
            'grade': 'Grade',
            'age': 'Age',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }