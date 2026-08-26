from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject1': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject2': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject3': forms.NumberInput(attrs={'class': 'form-control'}),
        }