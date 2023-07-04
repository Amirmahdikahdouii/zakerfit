from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone Number must be set")
        if "first_name" not in extra_fields.keys() or "last_name" not in extra_fields.keys():
            raise ValueError("Full name must be set")
        if password is None:
            raise ValueError("Password must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone_number, password, **extra_fields)
