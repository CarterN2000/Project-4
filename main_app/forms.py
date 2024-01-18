from django.forms import ModelForm, DateInput, TextInput, NumberInput
from .models import Workout, Exercise

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'sets': NumberInput(attrs={'class': 'form-control'}),
            'reps': NumberInput(attrs={'class': 'form-control'}),
            'weight': NumberInput(attrs={'class': 'form-control'}),
        }

class CreateWorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'date']
        widgets= {
         'date': DateInput(attrs={
             'type': 'date',

             }),
         }
