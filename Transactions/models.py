from django.db import models
from django.contrib.auth import get_user_model
from Accounts.utils import ShamsiDateTimeField, ShamsiDateField
from .utils import user_transaction_image_path


class UserTransactionStatusChoices(models.IntegerChoices):
    PENDING = 1, "در انتظار پرداخت"
    PAYED = 2, "پرداخت شده"
    FAILED = 3, "پرداخت ناموفق"
    CONFIRMATION = 4, "در انتظار تایید"


class UserPaymentWayChoices(models.IntegerChoices):
    ONLINE_PAY = 1, "درگاه پرداخت"
    OFFLINE_PAY = 2, "رسید واریز"


class UserPaymentForChoices(models.IntegerChoices):
    PRIVATE_ONLINE_CLASS = 1, "کلاس آنلاین خصوصی"
    PUBLIC_ONLINE_CLASS = 2, "کلاس آنلاین گروهی"
    TIME = 3, "تایم های حضوری کراسفیت"
    CROSSFIT_PROGRAMS = 4, "برنامه های کراسفیت"
    FOOD_PROGRAMS = 5, "برنامه تغذیه"


class UserTransaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="transactions")
    price = models.PositiveIntegerField()
    create_date = ShamsiDateTimeField(auto_now_add=True)
    payment_status = models.PositiveSmallIntegerField(choices=UserTransactionStatusChoices.choices, default=1)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_way = models.PositiveSmallIntegerField(choices=UserPaymentWayChoices.choices, null=True, blank=True)
    last_update_date = models.DateTimeField(auto_now=True, auto_created=True)
    payment_for = models.PositiveSmallIntegerField(choices=UserPaymentForChoices.choices, default=3)

    def __str__(self):
        return self.user.get_full_name()


class UserOfflinePayment(models.Model):
    transaction = models.ForeignKey(UserTransaction, on_delete=models.CASCADE, related_name="offline_payments")
    picture = models.ImageField(upload_to=user_transaction_image_path, )
    date = ShamsiDateTimeField(auto_now_add=True)
    payment_date = ShamsiDateField(null=True, blank=True)
    confirmed_by_admin = models.BooleanField(default=False)
    admin = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        import jdatetime
        return jdatetime.date.fromgregorian(year=self.date.year, month=self.date.month, day=self.date.day).strftime(
            "%Y/%m/%d")
