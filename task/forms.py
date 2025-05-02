from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter task title'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full sm:w-1/3 p-2 border rounded'
            }),
        }
