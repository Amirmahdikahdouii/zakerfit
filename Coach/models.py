from django.db import models
from django.contrib.auth import get_user_model
from Accounts.utils import ShamsiDateField


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
    slug = models.SlugField(null=True, blank=True)
    coach_info = models.CharField(max_length=400, null=True, blank=True)
    join_date = ShamsiDateField(null=True, blank=True)
    work_experience = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.en_name

    def coach_detail_view_path(self):
        from django.shortcuts import reverse
        if self.slug is None:
            return reverse("Coaches:coach_index")
        return reverse("Coaches:coach_detail", kwargs={"slug": self.slug})

    def get_join_date(self):
        if self.join_date is None:
            return None
        return str(self.join_date).replace("-", "/")


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


class CoachSocialMediaTypes(models.IntegerChoices):
    INSTAGRAM = 1, "instagram"
    TWITTER = 2, "twitter"
    TELEGRAM = 3, "telegram"
    FACEBOOK = 4, "facebook"


class CoachSocialMedia(models.Model):
    social_media = models.PositiveSmallIntegerField(choices=CoachSocialMediaTypes.choices)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name="social_medias")
    url = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.get_social_media_display()} - {self.coach.en_name}"


class CoachAbility(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name="abilities")
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}-{self.coach.name}"
