from django.urls import path
from . import views

app_name = "Accounts"
urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogOutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("coach-profile/", views.CoachProfileView.as_view(), name="coach-profile"),
    path("coach-profile/times/", views.CoachProfileTimesView.as_view(), name="coach-profile-times"),
    path("coach-profile/times/change-coach/<int:id>/", views.CoachProfileTimesChangeCoachView.as_view(),
         name="coach-profile-times-change-coach"),
    path("coach-profile/times/change-place-count/", views.CoachProfileTimesChangePlaceCountView.as_view(),
         name="coach-profile-times-change-place-count"),
    path("change-user-profile/", views.ChangeUserProfileView.as_view(), name="change_user_profile"),
    path("change-user-birthday/", views.ChangeUserBirthdayView.as_view(), name="change_user_birthday"),
    path("change-user-gender/", views.ChangeUserGenderView.as_view(), name="change_user_gender"),
    path("register-present-class/", views.RegisterPresentClassView.as_view(), name="register_present_class"),
    path("register-present-class/<int:id>/", views.RegisterPresentClassView.as_view(),
         name="submit_register_present_class"),
    path("change-present-class/", views.ChangePresentClassView.as_view(), name="change_present_class"),
    path("change-present-class/<int:id>/", views.ChangePresentClassView.as_view(), name="submit_change_present_class"),
    path('verify-phone-number/', views.VerifyPhoneNumberView.as_view(), name='verify_phone_number_view'),
]
