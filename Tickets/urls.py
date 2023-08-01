from django.urls import path
from . import views

app_name = "Tickets"
urlpatterns = [
    path('anonymous_users_question/', views.AnonymousUsersQuestionCreateView.as_view(), name="anonymous_user_question"),
    path('user-tickets/', views.UserTicketsView.as_view(), name="user_tickets"),
    path('user-tickets/add', views.CreateUserQuestionView.as_view(), name="create_user_question"),
]
