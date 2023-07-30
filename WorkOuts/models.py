from django.db import models
from Accounts.utils import ShamsiDateField
from django.utils.timezone import now


class Workout(models.Model):
    name = models.CharField(max_length=400)
    en_name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class DailyPlanTypes(models.IntegerChoices):
    FOR_TIME = 1, "FOR_TIME"
    AMRAP = 2, "AMRAP"
    EMOM = 3, "EMOM"
    E2MOM = 4, "E2MOM"
    TABATA = 5, "TABATA"
    OTHER = 6, "OTHER"


class DailyPlan(models.Model):
    date = ShamsiDateField(default=now())
    name = models.CharField(max_length=200)
    plan_type = models.PositiveSmallIntegerField(choices=DailyPlanTypes.choices)
    time_cap = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)

    def get_date(self):
        import jdatetime
        return str(jdatetime.date.fromgregorian(
            year=self.date.year,
            month=self.date.month,
            day=self.date.day
        )).replace("-", "/")

    def __str__(self):
        return f"{self.name} - {self.get_date()}"


class DailyPlanWorkout(models.Model):
    plan = models.ForeignKey(DailyPlan, on_delete=models.CASCADE, related_name="workouts")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="daily_plan_workouts")
    count = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"{self.workout.name}, {self.plan}"
