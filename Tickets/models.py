from django.db import models
from Accounts.utils import IranPhoneNumberValidator, ShamsiDateTimeField, ShamsiDateField
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


class UserQuestion(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=400)
    message = models.TextField()
    created_at = ShamsiDateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    checked_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="checked_questions")

    def __str__(self):
        return f"{self.title}, {self.user.get_full_name()}"

    def get_date(self):
        import jdatetime
        return jdatetime.date(year=self.created_at.year, month=self.created_at.month, day=self.created_at.day).strftime(
            "%Y/%mm/%d")


class UserQuestionReply(models.Model):
    question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="question_replies")
    message = models.TextField()
    created_at = ShamsiDateField(auto_now_add=True)
    is_user_reply = models.BooleanField(default=False)
    parent_answer = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)

    def __str__(self):
        return self.author.get_full_name()

    def get_date(self):
        import jdatetime
        return jdatetime.date(year=self.created_at.year, month=self.created_at.month, day=self.created_at.day).strftime(
            "%Y/%mm/%d")
