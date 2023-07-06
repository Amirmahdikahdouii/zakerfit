from django.db import models
from .managers import TimeManager


class Time(models.Model):
    title = models.CharField(max_length=500)
    place_count = models.PositiveSmallIntegerField()
    athlete_count = models.PositiveSmallIntegerField(default=0, blank=True)
    has_place_remain = models.BooleanField(default=True)
    class_name = models.CharField(max_length=150, null=True, blank=True, default="کراسفیت")
    coach_name = models.CharField(max_length=200, null=True, blank=True, default="محمدرضا ذاکری")

    objects = TimeManager()

    def __str__(self):
        return self.title

    @property
    def place_remain(self):
        return self.place_count - self.athlete_count

    def get_place_remain_percentage(self):
        return self.athlete_count * 100 // self.place_count
