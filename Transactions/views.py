from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import UserTransaction, UserOfflinePayment, OnlineClassTransaction
from .forms import UserOfflinePaymentForm


class UserTransactionsListView(LoginRequiredMixin, ListView):
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


class UserChoosePaymentWayView(LoginRequiredMixin, DetailView):
    template_name = "Transactions/choose_payment.html"
    model = UserTransaction

    def get_queryset(self):
        queryset = self.model.objects.filter(user_id=self.request.user.id, payment_status=1)
        if not queryset.exists():
            messages.error(self.request, "شما اجازه دسترسی به این پرداخت را ندارید")
        return queryset


class UserOfflinePaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "Transactions/offline_payment_form.html"
    form_class = UserOfflinePaymentForm
    context_object_name = "form"
    model = UserOfflinePayment
    success_url = reverse_lazy("Transactions:user-transactions")
    success_message = "فیش واریزی با موفقیت ثبت شد"

    def dispatch(self, request, *args, **kwargs):
        transaction_id = self.kwargs.get("pk")
        try:
            if request.user.is_authenticated:
                transaction = UserTransaction.objects.get(id=transaction_id, user=request.user, payment_status=1)
        except UserTransaction.DoesNotExist:
            messages.warning(request, "تراکنش یافت نشد")
            return redirect("Transactions:user-transactions")
        self.extra_context = {"transaction_id": transaction_id}
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        import jdatetime
        pk = self.kwargs.get("pk")
        payment_date = self.request.POST.get("payment_date")
        payment_date = list(map(int, payment_date.split("/")))
        transaction = UserTransaction.objects.filter(user=self.request.user, payment_status=1, id=pk)
        if not transaction.exists():
            messages.error(self.request, "خطا، لطفا تراکنش انجام شده مربوط به خودتان را انتخاب کنید.")
            raise Http404("رکورد مورد نظر یافت نشد")
        transaction = transaction.first()
        transaction.payment_status = 4
        transaction.payment_way = 2
        transaction.save()
        form.instance.transaction = transaction
        form.instance.payment_date = jdatetime.date(year=payment_date[0], month=payment_date[1],
                                                    day=payment_date[2]).togregorian()
        return super().form_valid(form)


class CreateOnlineClassTransactionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        from Classes.models import OnlineClass
        try:
            online_class_id = int(request.POST.get("class_id"))
            if request.user.online_class_transactions.filter(online_class_id=online_class_id).exists():
                messages.warning(request, "لطفا تراکنش خود را پرداخت کنید")
                return redirect("Transactions:choose_payment", pk=request.user.online_class_transactions.filter(
                    online_class_id=online_class_id).last().transaction.id)
            online_class = OnlineClass.objects.get(id=online_class_id)
            online_class_type = online_class.class_type.class_type
            if online_class_type == 1:
                transaction_type = 6
            elif online_class_type == 3:
                transaction_type = 1
            else:
                transaction_type = online_class_type
        except (ValueError, OnlineClass.DoesNotExist):
            messages.error(request, "لطفا اطلاعات کلاس را با دقت وارد کنید.")
            return redirect("Home:home_view")
        transaction = UserTransaction.objects.create(
            user=request.user, price=online_class.price, payment_for=transaction_type
        )
        OnlineClassTransaction.objects.create(online_class=online_class, user=request.user, transaction=transaction)
        messages.success(request, "لطفا شیوه پرداخت را انتخاب کنید.")
        return redirect("Transactions:choose_payment", pk=transaction.id)
