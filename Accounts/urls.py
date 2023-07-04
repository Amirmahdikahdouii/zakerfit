from django.urls import path
from . import views

app_name = "Accounts"
urlpatterns = [
    path("sign-up/", views.signup, name="sign-up"),
]
