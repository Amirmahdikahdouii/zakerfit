from django.contrib import admin
from .models import Time


class TimeAdmin(admin.ModelAdmin):
    class Meta:
        model = Time

    list_display = ("__str__", "athlete_count", 'has_place_remain')
    list_filter = ("has_place_remain",)


admin.site.register(Time, TimeAdmin)
