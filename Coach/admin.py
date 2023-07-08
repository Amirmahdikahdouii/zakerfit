from django.contrib import admin
from .models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")
    list_filter = ("is_active",)


admin.site.register(Coach, CoachAdmin)
