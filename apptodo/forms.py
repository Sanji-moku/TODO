from django import forms
from apptodo.models import Task

class TaskForm(forms.ModelForm):
    texte = forms.CharField(label='',widget= forms.TextInput
                           (attrs={
                                'placeholder':'Ajouter une tâche ',
                                'class': 'form-control'
                            }))
    class Meta:
        model = Task
        fields = ['texte',]
