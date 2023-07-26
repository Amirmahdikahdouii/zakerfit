from django.db import models
from Accounts.utils import IranPhoneNumberValidator, ShamsiDateField
from Coach.models import Coach


class AnonymousUsersQuestion(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(null=True, blank=True, max_length=300)
    phone_number = models.CharField(max_length=11, validators=[IranPhoneNumberValidator, ])
    message = models.TextField()
    date = ShamsiDateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    is_answered = models.BooleanField(default=False)
    answered_by = models.ForeignKey(Coach, on_delete=models.SET_NULL, related_name="anonymous_user_questions",
                                    null=True, blank=True)

    def __str__(self):
        return self.name
