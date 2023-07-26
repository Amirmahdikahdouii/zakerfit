from django.urls import path
from . import views

app_name = "Tickets"
urlpatterns = [
    path('anonymous_users_question/', views.AnonymousUsersQuestionCreateView.as_view(), name="anonymous_user_question"),
]
