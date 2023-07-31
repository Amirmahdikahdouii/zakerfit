from django.urls import path
from . import views

app_name = "Workouts"
urlpatterns = [
    path("daily-plan/", views.DailyWorkoutView.as_view(), name="daily_plan"),
]
