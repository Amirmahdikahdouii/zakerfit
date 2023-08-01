from django.contrib import admin
from .models import AnonymousUsersQuestion, UserQuestion, UserQuestionReply


class AnonymousUsersQuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_checked", "is_answered", "date", "last_checked_date")
    list_filter = ("is_checked", "is_answered")
    ordering = ("-date",)


class UsersQuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_checked", "created_at")
    list_filter = ("is_checked",)
    ordering = ("-created_at",)


admin.site.register(AnonymousUsersQuestion, AnonymousUsersQuestionAdmin)
admin.site.register(UserQuestion, UsersQuestionAdmin)
