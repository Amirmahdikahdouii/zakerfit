from django.urls import path
from . import views

app_name = "Coaches"
urlpatterns = [
    path('', views.CoachIndexView.as_view(), name="coach_index"),
    path('<slug:slug>', views.CoachDetailView.as_view(), name="coach_detail"),
]
