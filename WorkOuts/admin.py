from django.contrib import admin
from .models import Workout, DailyPlan, DailyPlanWorkout, UserPlanRecord

admin.site.register(Workout)
admin.site.register(DailyPlan)
admin.site.register(DailyPlanWorkout)
admin.site.register(UserPlanRecord)
