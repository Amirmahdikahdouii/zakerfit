from django.contrib import admin
from .models import Time, ClassType, ClassCategory, OnlineClass, OnlineClassTime, OnlineClassBenefit


class TimeAdmin(admin.ModelAdmin):
    class Meta:
        model = Time

    list_display = ("__str__", "athlete_count", 'has_place_remain')
    list_filter = ("has_place_remain",)
    prepopulated_fields = {"slug": ("en_title",)}


class OnlineClassAdmin(admin.ModelAdmin):
    list_display = ("__str__", "class_type", "is_active")
    list_filter = ("is_active", "class_type")

    class Meta:
        model = OnlineClass


admin.site.register(Time, TimeAdmin)
admin.site.register(ClassType)
admin.site.register(ClassCategory)
admin.site.register(OnlineClass, OnlineClassAdmin)
admin.site.register(OnlineClassTime)
admin.site.register(OnlineClassBenefit)
