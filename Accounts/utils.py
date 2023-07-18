from django.db import models
from django.core.validators import RegexValidator
from django.contrib import messages
from django.shortcuts import redirect


class IranPhoneNumberValidator(RegexValidator):
    def __init__(self):
        regex = r'^(\+98|0)?9\d{9}$'
        message = 'Enter a Valid Iran Phone Number'
        super().__init__(regex=regex, message=message)


class ShamsiDateField(models.DateField):
    def from_db_value(self, value, expression, connection):
        """
        this method is responsible for converting the date stored in the database to the corresponding Shamsi date.
        """
        if value is None:
            return value
        import jdatetime
        if value.year < 1400:
            return jdatetime.date(year=value.year, month=value.month, day=value.day)
        return jdatetime.date.fromgregorian(year=value.year, month=value.month, day=value.day)

    def to_python(self, value):
        import jdatetime
        import datetime
        if isinstance(value, datetime.date):
            return jdatetime.date(year=value.year, month=value.month, day=value.day)
        return None

    def get_prep_value(self, value):
        if value is None:
            return None
        import jdatetime
        return jdatetime.date(value.year, value.month, value.day)


class IsAdminRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            messages.error(request, "فقط مربیان اجازه دسترسی به این صفحه را دارند!")
            return redirect("Accounts:profile")
        return super().dispatch(request, *args, **kwargs)
