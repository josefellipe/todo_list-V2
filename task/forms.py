from django import forms
from .models import Task
from .choices import STATUS_CHOICES, PRIORITY_CHOICES, OWNER_CHOICES

class TaskForm(forms.ModelForm):
    owner = forms.ChoiceField(
        label='Owner',
        choices=OWNER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        })
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        })
    )

    priority = forms.ChoiceField(
        label='Priority',
        choices=PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    status = forms.ChoiceField(
        label='Status',
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ['owner', 'title', 'description', 'priority', 'status']
