from django.db import models
from django.contrib.auth import get_user_model


def change_coach_image_name(instance, filename):
    import os
    import random
    ext = filename.split(".")[-1]
    name = f"{instance.en_name}-{random.randint(10, 99)}.{ext}"
    return os.path.join("Coach/Pictures/", name)


class Coach(models.Model):
    name = models.CharField(max_length=400)
    en_name = models.CharField(max_length=400)
    picture = models.ImageField(upload_to=change_coach_image_name, null=True, blank=True)
    about = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.en_name


class RateChoices(models.IntegerChoices):
    VERY_GOOD = 5, 'VERY_GOOD'
    GOOD = 4, "GOOD"
    NORMAL = 3, "NORMAL"
    BAD = 2, "BAD"
    VERY_BAD = 1, "VERY_BAD"


class CoachRate(models.Model):
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE, related_name="rates")
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="coach_rates",
                                related_query_name="coach_rated_by")
    rate = models.PositiveSmallIntegerField(choices=RateChoices.choices)

    def __str__(self):
        return f"{self.user.first_name}-{self.coach.name}"
