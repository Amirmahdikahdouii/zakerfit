from django.contrib import admin
from .models import AnonymousUsersQuestion


class AnonymousUsersQuestionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_checked", "is_answered", "date")
    list_filter = ("is_checked", "is_answered")
    ordering = ("-date",)


admin.site.register(AnonymousUsersQuestion, AnonymousUsersQuestionAdmin)
