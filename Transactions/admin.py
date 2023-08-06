from django.contrib import admin
from .models import UserTransaction, UserOfflinePayment, OnlineClassTransaction


@admin.register(UserTransaction)
class UserTransactionsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "payment_status", "last_update_date", "payment_for")
    list_filter = ("payment_status", "payment_for")


@admin.register(UserOfflinePayment)
class UserOfflinePaymentsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "confirmed_by_admin",)
    list_filter = ("confirmed_by_admin",)


admin.site.register(OnlineClassTransaction)
