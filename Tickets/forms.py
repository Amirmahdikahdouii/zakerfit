from django import forms
from .models import AnonymousUsersQuestion, UserQuestion, UserQuestionReply
from Accounts.utils import IranPhoneNumberValidator


class AnonymousUsersQuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-input"
            if field_name == "phone_number":
                phone_validator = IranPhoneNumberValidator()
                field.validators.append(phone_validator)
                field.widget.attrs['placeholder'] = "شماره همراه"
            elif field_name == "name":
                field.widget.attrs['placeholder'] = "نام و نام خانوادگی"
            elif field_name == "email":
                field.widget.attrs['placeholder'] = "ایمیل"
            elif field_name == "message":
                field.widget.attrs['placeholder'] = "متن پیام..."

    class Meta:
        model = AnonymousUsersQuestion
        fields = ("name", "email", "phone_number", "message")
        error_messages = {
            "name": {
                "max_value": "حداکثر 1000 کاراکتر مجاز است"
            },
            "phone_number": {
                "invalid": "لطفا شماره تلفن خود را به صورت شماره ایران وارد کنید. مثال:09121234567"
            },
            "email": {
                "invalid": "لطفا ایمیل را به صورت صحیح وارد گنید.",
                "max_length": "حداکثر تعداد کاراکتر ایمیل 300 کاراکتر است."
            }
        }

        help_texts = {
            "email": "وارد کردن ایمیل ضروری نیست"
        }


class UpdateAnonymousTicketStatusForm(forms.ModelForm):
    class Meta:
        model = AnonymousUsersQuestion
        fields = ("is_checked", "is_answered")


class UserQuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserQuestion
        fields = ("title", "message")
