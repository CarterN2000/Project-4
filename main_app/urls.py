from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('workouts/history/', views.history, name='history'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('workouts/create/', views.CreateWorkout.as_view(), name='create_workout'),
    path('workouts/<int:pk>/update/', views.UpdateWorkout.as_view(), name='update_workout'),
    path('workouts/<int:pk>/delete/', views.DeleteWorkout.as_view(), name='delete_workout'),
    path('workouts/<int:workout_id>/add_exercise/', views.add_exercise, name='add_exercise'),
    path('accounts/signup/', views.signup, name='signup'),
    path('workouts/<int:workout_id>/find_best/', views.get_max_exercises, name='find_exercise_max'),
    # path('workouts/find_best/', views.FindMaxExercises.as_view(), name='find_exercise_max'),
]