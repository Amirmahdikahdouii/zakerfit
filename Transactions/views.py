from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTransaction
from django.urls import reverse_lazy


class UserTransactionsListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("Accounts:login")
    model = UserTransaction
    template_name = "Transactions/user_transactions.html"
    context_object_name = "user_transactions"

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).order_by("-id")
