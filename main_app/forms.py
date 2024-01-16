from django.forms import ModelForm, DateInput
from .models import Workout, Exercise

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight']

class CreateWorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'
        widgets= {
         'date': DateInput(attrs={'type': 'date'}),
         }