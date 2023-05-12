from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
   due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'due_date'}))

class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'due_date', 'priority']
        widgets = {
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
