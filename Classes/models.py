from django.db import models
from .managers import TimeManager, OnlineClassManager
from Accounts.utils import ShamsiDateField


class ClassCategory(models.Model):
    """
    This Model Provides class category such as ['crossfit', 'gymnastic', 'weight-lifting', ...]
    """
    name = models.CharField(max_length=400)
    slug = models.SlugField()
    image = models.ImageField(upload_to="Classes/categories/", null=True, blank=True)

    def __str__(self):
        return self.name

    def has_image(self):
        return True if self.image.name else False

    @property
    def category_classes_url(self):
        from django.shortcuts import reverse
        return reverse("Classes:classes_category_filter", kwargs={"slug": self.slug})


class ClassTypesChoices(models.IntegerChoices):
    PRESET_CLASS = 1, "کلاس حضوری"
    GROUP_ONLINE_CLASS = 2, "کلاس آنلاین گروهی"
    PRIVATE_ONLINE_CLASS = 3, "کلاس آنلاین خصوصی"


class ClassType(models.Model):
    """
    This Model is based and separate the classes by Online and present class
    """
    class_type = models.PositiveSmallIntegerField(choices=ClassTypesChoices.choices, default=2)

    def __str__(self):
        return "کلاس حضوری" if self.class_type == 1 else "کلاس آنلاین گروهی" if self.class_type == 2 else \
            "کلاس آنلاین خصوصی"


class Time(models.Model):
    title = models.CharField(max_length=500)
    en_title = models.CharField(max_length=300, null=True, blank=True)
    place_count = models.PositiveSmallIntegerField()
    athlete_count = models.PositiveSmallIntegerField(default=0, blank=True)
    has_place_remain = models.BooleanField(default=True)
    coach = models.ForeignKey("Coach.Coach", on_delete=models.SET_NULL, null=True, blank=True,
                              related_name="crossfit_times")
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(ClassCategory, on_delete=models.SET_NULL, null=True, blank=True)
    class_type = models.ForeignKey(ClassType, on_delete=models.SET_NULL, null=True, blank=True)

    objects = TimeManager()

    def __str__(self):
        return self.title

    @property
    def place_remain(self):
        if isinstance(self.athlete_count, int):
            return self.place_count - self.athlete_count
        return "نامشخص"

    def get_place_remain_percentage(self):
        return self.athlete_count * 100 // self.place_count

    @property
    def class_name(self):
        return self.category.name

    @property
    def coach_name(self):
        return self.coach.name if self.coach is not None else ""


class OnlineClass(models.Model):
    objects = OnlineClassManager()

    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="Classes/Online-Class/")
    coach = models.ForeignKey("Coach.Coach", null=True, blank=True, on_delete=models.SET_NULL,
                              related_name="online_classes")
    slug = models.SlugField()
    start_time = ShamsiDateField(null=True, blank=True)
    place_count = models.PositiveSmallIntegerField(null=True, blank=True)
    athlete_count = models.PositiveSmallIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)
    sessions_count = models.PositiveSmallIntegerField(null=True, blank=True)
    sessions_count_in_week = models.PositiveSmallIntegerField(null=True, blank=True)
    # Sessions Duration in minutes:
    sessions_duration = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    category = models.ForeignKey(ClassCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="online_classes")
    class_type = models.ForeignKey(ClassType, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="online_classes")

    def __str__(self):
        return f"{self.get_class_type_name()} {self.title}"

    @property
    def place_remain(self):
        if isinstance(self.athlete_count, int) and isinstance(self.place_count, int):
            return self.place_count - self.athlete_count

    def has_place(self):
        return True if self.place_count is not None else False

    def get_place_remain_percentage(self):
        return self.athlete_count * 100 // self.place_count

    def get_class_url(self):
        from django.shortcuts import reverse
        if self.get_class_type() == 2:
            return reverse("Classes:group_class_view", kwargs={"slug": self.slug})
        elif self.get_class_type() == 3:
            return reverse("Classes:private_class_view", kwargs={"slug": self.slug})

    def get_class_type(self):
        return self.class_type.class_type

    def get_class_type_name(self):
        return "کلاس آنلاین گروهی" if self.get_class_type() == 2 \
            else "کلاس آنلاین خصوصی" if self.get_class_type() == 3 else "کلاس حضوری"

    def get_class_type_url(self):
        from django.shortcuts import reverse
        if self.get_class_type() == 2:
            return reverse("Classes:group_classes")
        elif self.get_class_type() == 3:
            return reverse("Classes:private_classes")

    def get_start_time(self):
        import jdatetime
        if self.start_time is None:
            return None
        return str(
            jdatetime.date.fromgregorian(year=self.start_time.year, month=self.start_time.month,
                                         day=self.start_time.day)).replace("-", "/")

    def get_price(self):
        return "{:,}".format(self.price)

    def class_has_time(self):
        return True if self.times.count() > 0 else False

    def has_image(self):
        return True if self.image.name else False


class OnlineClassBenefit(models.Model):
    """
    This Model, Make a benefits table for classes and save the features that users will have if they join the class.
    """
    _class = models.ForeignKey(OnlineClass, on_delete=models.CASCADE, related_name="benefits")
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class OnlineClassTimeDayChoices(models.IntegerChoices):
    SATURDAY = 1, "شنبه"
    SUNDAY = 2, "یکشنبه"
    MONDAY = 3, "دوشنبه"
    TUESDAY = 4, "سه شنبه"
    WEDNESDAY = 5, "چهارشنبه"
    THURSDAY = 6, "پنجشنبه"
    FRIDAY = 7, "جمعه"

    @staticmethod
    def get_dict_days():
        return [
            {'day': 'شنبه', 'id': 1},
            {'day': 'یکشنبه', 'id': 2},
            {'day': 'دوشنبه', 'id': 3},
            {'day': 'سه شنبه', 'id': 4},
            {'day': 'چهارشنبه', 'id': 5},
            {'day': 'پنجشنبه', 'id': 6},
            {'day': 'جمعه', 'id': 7}
        ]


class OnlineClassTime(models.Model):
    """
    This Model is for online class times table and save each time of table in a seperated row.
    """
    _class = models.ForeignKey(OnlineClass, on_delete=models.CASCADE, related_name="times")
    day = models.PositiveSmallIntegerField(choices=OnlineClassTimeDayChoices.choices)
    time = models.CharField(max_length=200)

    def __str__(self):
        return f"{self._class.title}-{self.day}-{self.time}"

    def get_day(self):
        for day in OnlineClassTimeDayChoices.get_dict_days():
            if day['id'] == self.day:
                return day['day']


class TimePrice(models.Model):
    """
    This Model is For Present Classes in gym and their sessions count and prices.
    """
    price = models.PositiveIntegerField()
    sessions_count = models.PositiveSmallIntegerField(default=12)

    def __str__(self):
        return f" جلسات ماهانه: {self.sessions_count}"

    def get_price(self):
        price = self.price // 1000
        return "{:,}".format(price)

    def get_full_price(self):
        return "{:,}".format(self.price)


class PrivateClassesPreSubmit(models.Model):
    user = models.ForeignKey("Accounts.User", on_delete=models.CASCADE,
                             related_name="private_classes_pre_submits")
    private_class = models.ForeignKey(OnlineClass, on_delete=models.CASCADE,
                                      related_name="private_classes_pre_submit_users")

    def __str__(self):
        return f"{self.private_class.title}-{self.user.get_full_name()}"
