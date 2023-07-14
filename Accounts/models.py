from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from Classes.models import Time
from .utils import ShamsiDateField, IranPhoneNumberValidator
from django.contrib.auth import get_user_model


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
    join_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to=change_profile_name, null=True, blank=True)
    class_time = models.OneToOneField(Time, on_delete=models.SET_NULL, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    @property
    def is_staff(self):
        return self.is_superuser

    def has_profile_image(self):
        return True if self.profile_image is not None else False

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_gender(self):
        return "آقا" if self.gender == 1 else "خانم"


class UserPhoneNumberValidation(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="phone_validation")
    date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=6, null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.phone_number}-{self.is_verify}"
