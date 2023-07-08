from django.contrib import admin
from .models import Time, PrivateOnlineClass, GroupOnlineClass


class TimeAdmin(admin.ModelAdmin):
    class Meta:
        model = Time

    list_display = ("__str__", "athlete_count", 'has_place_remain')
    list_filter = ("has_place_remain",)
    prepopulated_fields = {"slug": ("en_title",)}


class PrivateOnlineClassAdmin(admin.ModelAdmin):
    class Meta:
        model = PrivateOnlineClass

    list_display = ("__str__",)


class GroupOnlineClassAdmin(admin.ModelAdmin):
    list_display = ("__str__", "athlete_count")

    class Meta:
        model = GroupOnlineClass


admin.site.register(Time, TimeAdmin)
admin.site.register(PrivateOnlineClass, PrivateOnlineClassAdmin)
admin.site.register(GroupOnlineClass, GroupOnlineClassAdmin)
