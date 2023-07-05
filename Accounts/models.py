from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from .managers import UserManager


class IranPhoneNumberValidator(RegexValidator):
    def __init__(self):
        regex = r'^(\+98|0)?9\d{9}$'
        message = 'Enterer a Valid Iran Phone Number'
        super().__init__(regex=regex, message=message)


class ShamsiDateField(models.DateField):
    def from_db_value(self, value, expression, connection):
        """
        this method is responsible for converting the date stored in the database to the corresponding Shamsi date.
        """
        if value is None:
            return value
        import jdatetime
        return jdatetime.date.fromgregorian(year=value.year, month=value.month, day=value.day)

    def to_python(self, value: dict):
        import jdatetime
        import datetime
        if isinstance(value, dict):
            return jdatetime.date(value['year'], value['month'], value['day']).togregorian()
        elif isinstance(value, datetime.date):
            return jdatetime.date.fromgregorian(year=value.year, month=value.month, day=value.day)
        return None

    def get_prep_value(self, value):
        if value is None:
            return None
        import jdatetime
        return jdatetime.date(value.year, value.month, value.day).togregorian()


class UserGenderChoices(models.IntegerChoices):
    MALE = 1, "MALE"
    FEMAIL = 2, "FEMAIL"


def change_profile_name(instance, filename):
    """
    This Function change the profile image name and save it into destination
    """
    import os
    import random
    ext = filename.split(".")[-1]
    unique_file_name = f"{instance.last_name}-{random.randint(1000, 9999)}.{ext}"
    return os.path.join("users/profile-images/", unique_file_name)


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=13, unique=True, validators=[IranPhoneNumberValidator()])
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = ShamsiDateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    gender = models.PositiveSmallIntegerField(choices=UserGenderChoices.choices, default=UserGenderChoices.MALE)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to=change_profile_name, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_profile_image(self):
        return True if self.profile_image is not None else False

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_gender(self):
        return "آقا" if self.gender == 1 else "خانم"
