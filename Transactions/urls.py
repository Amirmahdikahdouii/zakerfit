from django.urls import path
from . import views

app_name = "Transactions"
urlpatterns = [
    path("user-transactions/", views.UserTransactionsListView.as_view(), name="user-transactions"),
    path("choose-payment/<int:pk>/", views.UserChoosePaymentWayView.as_view(), name="choose_payment"),
    path("offline-payment/<int:pk>/", views.UserOfflinePaymentCreateView.as_view(), name="offline_payment"),
]
