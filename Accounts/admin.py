from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import Group
from .forms import UserCreationForm, UserChangeForm
from .models import (User, UserPhoneNumberValidation, PresentClass, UserTimePayment, UserTimeSessionsExpire,
                     UserTimePaymentFactors)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['__str__', 'phone_number', 'is_superuser']
    list_filter = ['is_superuser']
    fieldsets = [
        (None, {"fields": ["phone_number", 'email', 'password']}),
        ("Personal Info", {"fields": ["first_name", "last_name", "birthday", "gender", 'profile_image']}),
        ("Permissions", {"fields": ['is_superuser', "is_admin", "last_login", "groups", "user_permissions"]}),
        ("Classes", {"fields": ['class_time']})
    ]
    add_fieldsets = [
        (None, {
            "classes": ["wide"],
            "fields": ['phone_number', 'first_name', "last_name", 'password1', 'password2', ]
        })
    ]

    search_fields = ['first_name', 'last_name']
    ordering = ['-id']
    filter_horizontal = ["groups", "user_permissions"]


class UserPhoneNumberValidationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_verify")
    list_filter = ("is_verify",)


admin.site.register(User, UserAdmin)
admin.site.register(UserPhoneNumberValidation, UserPhoneNumberValidationAdmin)
admin.site.register(PresentClass)
admin.site.register(UserTimePayment)
admin.site.register(UserTimeSessionsExpire)
admin.site.register(UserTimePaymentFactors)
admin.site.unregister(Group)
