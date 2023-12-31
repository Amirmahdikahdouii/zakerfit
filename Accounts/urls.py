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
    path("coach-profile/times/<int:time_id>/athelets/", views.CoachProfileTimesAthletesView.as_view(),
         name="coach-profile-times-athletes"),
    path("coach-profile/times/<int:time_id>/athelets-presentation/",
         views.CoachProfileTimesAthletesPresentationView.as_view(),
         name="coach-profile-times-athletes-presentation"),
    path("coach-profile/times/athletes/<int:id>", views.CoachProfileTimeAthleteProfileView.as_view(),
         name="coach-athlete-profile"),
    path("coach-profile/times/add/", views.CoachProfileAddTimeView.as_view(),
         name="coach-add-time"),
    path("coach-profile/classes/", views.CoachProfileClassListView.as_view(),
         name="coach-class-list"),
    path("coach-profile/classes/add-class/", views.CoachProfileClassAddView.as_view(),
         name="coach-class-add"),
    path("coach-profile/classes/edit-class/<slug:slug>/", views.CoachProfileClassEditView.as_view(),
         name="coach-class-edit"),
    path("coach-profile/classes/edit-class/<slug:slug>/time/", views.CoachProfileClassEditTimesView.as_view(),
         name="coach-class-edit-times"),
    path("coach-profile/classes/add-category/", views.CoachProfileClassAddCategoryView.as_view(),
         name="coach-class-add-category"),
    path("coach-profile/classes/select-category/", views.CoachProfileClassSelectCategoryView.as_view(),
         name="coach-class-select-category"),
    path("coach-profile/classes/edit-category/<slug:slug>/", views.CoachProfileClassEditCategoryView.as_view(),
         name="coach-class-edit-category"),
    path("coach-profile/classes/<slug:slug>/", views.CoachProfileClassListView.as_view(),
         name="coach-class-list-filter"),
    path("coach-profile/tickets/", views.CoachProfileTicketsView.as_view(),
         name="coach-tickets"),
    path("coach-profile/tickets/anonymous-tickes/", views.CoachProfileAnonymousTicketsView.as_view(),
         name="coach-tickets-anonymous"),
    path("coach-profile/tickets/anonymous-tickes/<int:pk>/", views.CoachProfileAnonymousSingleTicketView.as_view(),
         name="coach-tickets-anonymous-detail"),
    path("coach-profile/tickets/anonymous-tickes/update/<int:pk>/",
         views.CoachProfileAnonymousSingleTicketUpdateView.as_view(),
         name="coach-tickets-anonymous-detail-update"),
    path("change-user-profile/", views.ChangeUserProfileView.as_view(), name="change_user_profile"),
    path("change-user-birthday/", views.ChangeUserBirthdayView.as_view(), name="change_user_birthday"),
    path("change-user-gender/", views.ChangeUserGenderView.as_view(), name="change_user_gender"),
    path("register-present-class/", views.RegisterPresentClassView.as_view(), name="register_present_class"),
    path("register-present-class/<int:id>/", views.RegisterPresentClassView.as_view(),
         name="submit_register_present_class"),
    path("delete-present-class/", views.DeletePresentClassView.as_view(), name="delete_present_class"),
    path("change-present-class/", views.ChangePresentClassView.as_view(), name="change_present_class"),
    path("change-present-class/<int:id>/", views.ChangePresentClassView.as_view(), name="submit_change_present_class"),
    path('verify-phone-number/', views.VerifyPhoneNumberView.as_view(), name='verify_phone_number_view'),
    path("time-payment/", views.TimePaymentView.as_view(), name="time_payment_form"),
    path("time-payment/confirm/", views.TimePaymentConfirmView.as_view(), name="time_payment_confirm"),
]
