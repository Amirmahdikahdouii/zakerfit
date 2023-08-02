from django.urls import path
from . import views

app_name = "Transactions"
urlpatterns = [
    path("user-transactions/", views.UserTransactionsListView.as_view(), name="user-transactions")
]
