from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


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
    name = forms.CharField(label='نام و نام خانوادگی', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی خود را وارد کنید'}))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))
    confirm_password = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))
