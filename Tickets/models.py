from django.db import models
from Accounts.utils import IranPhoneNumberValidator, ShamsiDateTimeField
from django.contrib.auth import get_user_model


class AnonymousUsersQuestion(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(null=True, blank=True, max_length=300)
    phone_number = models.CharField(max_length=11, validators=[IranPhoneNumberValidator, ])
    message = models.TextField()
    date = ShamsiDateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    last_checked_date = ShamsiDateTimeField(auto_now=True)
    is_answered = models.BooleanField(default=False)
    answered_date = ShamsiDateTimeField(null=True, blank=True)
    answered_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                    related_name="anonymous_user_questions",
                                    null=True, blank=True)

    def __str__(self):
        return self.name
