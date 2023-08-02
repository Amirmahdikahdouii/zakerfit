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
        status_filter = self.request.GET.get("filter_status")
        payment_filter = self.request.GET.get("filter_payment")
        if status_filter is None and payment_filter is None:
            return self.model.objects.filter(user_id=self.request.user.id).order_by("-id")
        elif payment_filter is None:
            return self.model.objects.filter(user_id=self.request.user.id, payment_status=status_filter).order_by("-id")
        elif status_filter is None:
            return self.model.objects.filter(user_id=self.request.user.id, payment_way=payment_filter).order_by("-id")
        else:
            return self.model.objects.filter(user_id=self.request.user.id, payment_way=payment_filter,
                                             payment_status=status_filter).order_by("-id")
