from django.urls import path
from . import views

app_name = "Accounts"
urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogOutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("change-user-profile/", views.ChangeUserProfileView.as_view(), name="change_user_profile"),
    path("change-user-birthday/", views.ChangeUserBirthdayView.as_view(), name="change_user_birthday"),
    path("change-user-gender/", views.ChangeUserGenderView.as_view(), name="change_user_gender"),
]
