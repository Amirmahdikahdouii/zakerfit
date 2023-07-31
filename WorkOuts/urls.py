from django.urls import path
from . import views

app_name = "Workouts"
urlpatterns = [
    path("daily-workouts-list/", views.DailyWorkoutListView.as_view(), name="daily_workouts_list"),
    path("plans/<int:pk>/", views.DailyWorkoutDetailView.as_view(), name="plan_detail"),
    path("daily-plan/", views.DailyWorkoutView.as_view(), name="daily_plan"),
]
