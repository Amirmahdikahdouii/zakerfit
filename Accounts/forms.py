from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import RegexValidator

password_regex_validation = RegexValidator(
    regex=r'^(?=.*[a-zA-Z]).{8,}$',
    message="پسورد باید حداقل 8 کاراکتر باشد و حروف را در بر بگیرد"
)


class UserCreationForm(forms.ModelForm):
    """
    Form to Create User By Admin in Admin Panel
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords Must be match!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    Forms to Update User information, including all fields for user, but replace the password field
    with Admins disabled password hash field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        exclude = ['join_date']


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='نام', max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}))
    phone_number = forms.CharField(
        label="تلفن همراه", max_length=13, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': "تلفن همراه خود را وارد کنید"}
        )
    )
    password = forms.CharField(label='رمز عبور', validators=[password_regex_validation],
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))
    confirm_password = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبور خود را با دقت وارد کنید")
        return password2


class LoginForm(forms.Form):
    phone_number = forms.CharField(
        label="تلفن همراه", max_length=13, widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': "تلفن همراه خود را وارد کنید"}
        )
    )
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))
