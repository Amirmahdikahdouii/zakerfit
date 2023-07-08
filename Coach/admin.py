from django.contrib import admin
from .models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("en_name",)}


admin.site.register(Coach, CoachAdmin)
