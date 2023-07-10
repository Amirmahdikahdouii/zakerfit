from django.db import models


class TimeManager(models.Manager):
    def add_athlete(self, time_id: int, count=1):
        try:
            time = self.get(id=time_id)
            time.athlete_count += count
            time.save()
            return time
        except self.DoesNotExists:
            raise ValueError("Time ID is does not exists")


class OnlineClassManager(models.Manager):
    def get_last_two_class(self):
        return self.filter(is_active=True).order_by("-id")[:2]
