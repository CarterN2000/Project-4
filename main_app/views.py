from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from .models import Workout, Exercise
from .forms import CreateWorkoutForm, ExerciseForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def history(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/history.html', {
        'workouts': workouts
    })

@login_required
def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    exercise_form  = ExerciseForm()
    
    best_exercise_id = request.GET.get('best_exercise_id')
    best_exercise = None

    best_reps_exercise_id = request.GET.get('best_reps_exercise_id')
    best_reps_exercise = None

    if best_exercise_id:
        best_exercise = get_object_or_404(Exercise, id=best_exercise_id)
    
    if best_reps_exercise_id:
        best_reps_exercise = get_object_or_404(Exercise, id=best_reps_exercise_id)

    return render(request, 'workouts/detail.html', {
        'workout': workout,
        'exercise_form': exercise_form,
        'best_exercise': best_exercise,
        'best_reps_exercise': best_reps_exercise,
    })

@login_required
def add_exercise(request, workout_id):
    form = ExerciseForm(request.POST)
    if form.is_valid():
        new_exercise = form.save(commit=False)
        new_exercise.workout_id = workout_id
        new_exercise.save()
    return redirect('workout_detail', workout_id=workout_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else: 
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def get_max_exercises(request, workout_id):
    query = request.GET.get('q')
    exercises = Exercise.objects.filter(
        Q(name__icontains=query)
    )

    best_weight = 0
    best_exercise = None

    best_weight_and_reps = 0
    best_reps_exercise = None

    for exercise in exercises:
        if exercise.weight > best_weight:
            best_weight = exercise.weight
            best_exercise = exercise
        if exercise.weight > best_weight_and_reps and exercise.reps > 5:
            best_weight_and_reps = exercise.weight
            best_reps_exercise = exercise
     
    if best_exercise and best_reps_exercise:
        # Pass the best_exercise and best_exercise_reps ID as a query parameter in the redirect URL
        redirect_url = reverse('workout_detail', args=[workout_id]) + f'?best_exercise_id={best_exercise.id}&best_reps_exercise_id={best_reps_exercise.id}'
        return redirect(redirect_url)
    elif best_exercise:
        # Maybe you only have a best exercise with less that 6 reps
        redirect_url = reverse('workout_detail', args=[workout_id]) + f'?best_exercise_id={best_exercise.id}'
        return redirect(redirect_url)
    else:
        # Exercise not found, add a message and redirect back to workout_detail
        messages.warning(request, "That exercise was not found in the database. Please check previous workouts to see what you called the exercise you are searching for.")
        return redirect('workout_detail', workout_id=workout_id)

class CreateWorkout(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = CreateWorkoutForm

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class UpdateWorkout(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['name', 'date']

class DeleteWorkout(LoginRequiredMixin, DeleteView):    
    model = Workout
    success_url = '/workouts/history'