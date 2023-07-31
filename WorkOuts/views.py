import datetime

from django.shortcuts import render
from .models import DailyPlan, DailyPlanWorkout, UserPlanRecord
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib import messages


@method_decorator(login_required, 'post')
class DailyWorkoutView(View):
    template_name = "Workouts/daily_workout.html"

    def get(self, request, *args, **kwargs):
        import datetime
        import jdatetime
        return render(request, self.template_name, {
            "plans": DailyPlan.objects.filter(date=datetime.date.today()),
            "date": jdatetime.date.today().strftime("%Y/%m/%d"),
        })

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if key.startswith("workout-"):
                try:
                    workout_id = int(key.split("workout-")[-1])
                    workout = DailyPlanWorkout.objects.get(id=workout_id)
                    record = int(value)
                    today_record = UserPlanRecord.objects.filter(date=datetime.date.today(), user=request.user,
                                                                 workout_id=workout_id)
                    if today_record.exists():
                        query = today_record.last()
                        query.record = record
                        query.save()
                        messages.success(request, "مقدار رکورد شما با موفقیت تغییر کرد")
                        return redirect("Workouts:daily_plan")
                    else:
                        UserPlanRecord.objects.create(workout=workout, user=request.user, record=record)
                    messages.success(request, "رکورد ها با موفقیت ثبت شد.")
                except (ValueError, DailyPlanWorkout.DoesNotExist):
                    messages.error(request, "خطا: مشکلی در اجرای برنامه وجود آمد.")
                    return redirect("Workouts:daily_plan")
        return redirect("Workouts:daily_plan")
