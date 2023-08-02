from django.db import models
from django.core.validators import RegexValidator
from django.contrib import messages
from django.shortcuts import redirect
import pytz
import datetime
import jdatetime


class IranPhoneNumberValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        regex = r'^(\+98|0)?9\d{9}$'
        message = 'Enter a Valid Iran Phone Number'
        super().__init__(**{'regex': regex, 'message': message})


class ShamsiDateField(models.DateField):
    def from_db_value(self, value, expression, connection):
        """
        this method is responsible for converting the date stored in the database to the corresponding Shamsi date.
        """
        if value is None:
            return value
        elif hasattr(value, "astimezone"):
            value = value.astimezone(pytz.timezone("Asia/Tehran"))
            return jdatetime.date.fromgregorian(year=value.year, month=value.month, day=value.day)
        return value

    def to_python(self, value):
        if value is None or isinstance(value, datetime.datetime):
            return value
        elif hasattr(value, "astimezone"):
            return value.astimezone(pytz.utc)
        return value

    def get_prep_value(self, value):
        if value is None:
            return None
        elif hasattr(value, "astimezone"):
            return value.astimezone(pytz.utc)
        return value


class ShamsiDateTimeField(models.DateTimeField):
    def from_db_value(self, value, expression, connection):
        """
        this method is responsible for converting the date stored in the database to the corresponding Shamsi date.
        """
        if value is None:
            return value
        elif value.year < 1500:
            value = value.astimezone(pytz.timezone("Asia/Tehran"))
            return jdatetime.datetime(year=value.year, month=value.month, day=value.day, hour=value.hour,
                                      minute=value.minute, second=value.second)
        elif hasattr(value, "astimezone"):
            value = value.astimezone(pytz.timezone("Asia/Tehran"))
            return jdatetime.datetime.fromgregorian(year=value.year, month=value.month, day=value.day, hour=value.hour,
                                                    minute=value.minute, second=value.second)
        return value

    def to_python(self, value):
        if value is None or isinstance(value, datetime.datetime):
            return value
        elif hasattr(value, "astimezone"):
            return value.astimezone(pytz.utc)
        return value

    def get_prep_value(self, value):
        if value is None:
            return None
        elif hasattr(value, "astimezone"):
            return value.astimezone(pytz.utc)
        return value


class IsAdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            messages.error(request, "فقط مربیان اجازه دسترسی به این صفحه را دارند!")
            return redirect("Accounts:profile")
        return super().dispatch(request, *args, **kwargs)
