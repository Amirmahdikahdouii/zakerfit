from django.db import models
from .managers import TimeManager
from Accounts.utils import ShamsiDateField


class Time(models.Model):
    title = models.CharField(max_length=500)
    en_title = models.CharField(max_length=300, null=True, blank=True)
    place_count = models.PositiveSmallIntegerField()
    athlete_count = models.PositiveSmallIntegerField(default=0, blank=True)
    has_place_remain = models.BooleanField(default=True)
    class_name = models.CharField(max_length=150, null=True, blank=True, default="کراسفیت")
    coach = models.OneToOneField("Coach.Coach", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="crossfit_times")
    slug = models.SlugField(null=True, blank=True)

    objects = TimeManager()

    def __str__(self):
        return self.title

    @property
    def place_remain(self):
        return self.place_count - self.athlete_count

    def get_place_remain_percentage(self):
        return self.athlete_count * 100 // self.place_count


class PrivateOnlineClass(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="Classes/Online-Class/")
    coach = models.OneToOneField("Coach.Coach", null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name="online_class")
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def is_online_class(self):
        return True

    def get_coach_name(self):
        return self.coach.name

    def get_class_url(self):
        from django.shortcuts import reverse
        return reverse("Classes:private_class_view", kwargs={"slug": self.slug})

    @staticmethod
    def get_class_type():
        return "کلاس آنلاین خصوصی"

    @staticmethod
    def get_class_type_url():
        from django.shortcuts import reverse
        return reverse("Classes:private_classes")


class GroupOnlineClass(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="Classes/Online-Class/")
    coach = models.OneToOneField("Coach.Coach", null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name="group_online_class")
    slug = models.SlugField()
    start_time = ShamsiDateField(null=True, blank=True)
    place_count = models.PositiveSmallIntegerField()
    athlete_count = models.PositiveSmallIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def place_remain(self):
        return self.place_count - self.athlete_count

    def get_place_remain_percentage(self):
        return self.athlete_count * 100 // self.place_count

    def get_class_url(self):
        from django.shortcuts import reverse
        return reverse("Classes:group_class_view", kwargs={"slug": self.slug})

    @staticmethod
    def get_class_type():
        return "کلاس آنلاین گروهی"

    @staticmethod
    def get_class_type_url():
        from django.shortcuts import reverse
        return reverse("Classes:group_classes")

    def get_start_time(self):
        return str(self.start_time).replace("-", "/")


class GroupClassBenefits(models.Model):
    _class = models.ForeignKey(GroupOnlineClass, on_delete=models.CASCADE, related_name="benefits")
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class PrivateClassBenefits(models.Model):
    _class = models.ForeignKey(PrivateOnlineClass, on_delete=models.CASCADE, related_name="benefits")
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class GroupOnlineClassTime(models.Model):
    _class = models.ForeignKey(GroupOnlineClass, on_delete=models.CASCADE, related_name="times")
    day = models.CharField(max_length=40)
    time = models.CharField(max_length=200)

    def __str__(self):
        return f"{self._class.title}-{self.day}-{self.time}"
