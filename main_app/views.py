from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from .forms import CreateWorkoutForm, ExerciseForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def history(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/history.html', {
        'workouts': workouts
    })

def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    exercise_form  = ExerciseForm()
    return render(request, 'workouts/detail.html', {
        'workout': workout,
        'exercise_form': exercise_form
    })

def add_exercise(request, workout_id):
    form = ExerciseForm(request.POST)
    if form.is_valid():
        new_exercise = form.save(commit=False)
        new_exercise.workout_id = workout_id
        new_exercise.save()
    return redirect('workout_detail', workout_id=workout_id)

class CreateWorkout(CreateView):
    print('Im here')
    model = Workout
    form_class = CreateWorkoutForm

class UpdateWorkout(UpdateView):
    model = Workout
    fields = '__all__'

class DeleteWorkout(DeleteView):    
    model = Workout
    success_url = '/workouts/history'