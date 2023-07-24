from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from Classes.models import Time
from .utils import ShamsiDateField, IranPhoneNumberValidator
from django.contrib.auth import get_user_model
import jdatetime


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


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=13, unique=True, validators=[IranPhoneNumberValidator()])
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = ShamsiDateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    gender = models.PositiveSmallIntegerField(choices=UserGenderChoices.choices, default=UserGenderChoices.MALE)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # We is_admin field also for filtering coaches
    is_admin = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to=change_profile_name, null=True, blank=True)
    class_time = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True, blank=True, related_name="athletes")

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    @property
    def is_staff(self):
        return self.is_admin

    def has_profile_image(self):
        return self.profile_image.name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_gender(self):
        return "آقا" if self.gender == 1 else "خانم"

    def get_join_date(self):
        import jdatetime
        date = jdatetime.date.fromgregorian(year=self.join_date.year, month=self.join_date.month,
                                            day=self.join_date.day)
        return str(date).replace("-", "/")


class UserPhoneNumberValidation(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="phone_validation")
    date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=6, null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.phone_number}-{self.is_verify}"


class PresentClass(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="class_present")
    time = models.ForeignKey("Classes.Time", on_delete=models.CASCADE, related_name="class_present")
    date = ShamsiDateField(auto_now=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()


class UserTimePayment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="time_payment")
    time = models.ForeignKey("Classes.Time", on_delete=models.SET_NULL, null=True, blank=True, related_name="payment")
    time_pricing = models.ForeignKey("Classes.TimePrice", on_delete=models.CASCADE, related_name="users_payment")
    date = ShamsiDateField(auto_now_add=True)
    sessions_remain = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.get_full_name()}: {self.date.month}/{self.date.day}"
