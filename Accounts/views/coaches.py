from django.shortcuts import render, redirect
from django.views import View
from Accounts.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from Accounts.utils import IsAdminRequiredMixin
from django.utils.text import slugify


class CoachProfileView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CoachProfileTimesView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get(self, request, *args, **kwargs):
        from Classes.models import Time
        times = Time.objects.all()
        options = ["مربی", "ظرفیت", "شاگردان", "حضور و غیاب"]
        return render(request, self.template_name, {"times": times, "options": options})


class CoachProfileTimesChangeCoachView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get(self, request, *args, **kwargs):
        from Coach.models import Coach
        from Classes.models import Time
        time = get_object_or_404(Time.objects.all(), id=kwargs.get('id'))
        coaches = Coach.objects.all()
        return render(request, self.template_name, {"coaches": coaches, "time": time})

    def post(self, request, *args, **kwargs):
        from Coach.models import Coach
        from Classes.models import Time
        coach_id = request.POST.get("coach_id", None)
        time = get_object_or_404(Time.objects.all(), id=kwargs.get('id'))
        if coach_id is None:
            coaches = Coach.objects.all()
            messages.error(request, "لطفا یکی از مربیان را انتخاب کنید")
            return render(request, self.template_name, {"coaches": coaches, "time": time})
        coach_id = int(coach_id)
        time.coach = get_object_or_404(Coach.objects.all(), id=coach_id)
        time.save()
        messages.success(request, "مربی با موفقیت تغییر کرد")
        return redirect("Accounts:coach-profile-times")


class CoachProfileTimesChangePlaceCountView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get_queryset(self):
        from Classes.models import Time
        return Time.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"times": self.get_queryset()})

    def post(self, request, *args, **kwargs):
        time_id = request.POST.get("time_id", None)
        new_place = request.POST.get("new_place", None)
        if time_id is None or new_place is None:
            messages.error(request, "لطفا اطلاعات را به درستی وارد کنید")
            return render(request, self.template_name, {"times": self.get_queryset()})
        time = get_object_or_404(self.get_queryset(), id=int(time_id))
        new_place = int(new_place)
        if new_place < time.place_count and time.athlete_count > new_place:
            messages.error(request, "تعداد ورزشکاران در این سانس بیشتر از تعداد ظرفیت انتخابی شماست!")
            return render(request, self.template_name, {"times": self.get_queryset()})
        time.place_count = new_place
        time.save()
        messages.success(request, "تغییر ظرفیت انجام شد")
        return redirect("Accounts:coach-profile-times")


class CoachProfileTimesAthletesView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get_queryset(self):
        from Classes.models import Time
        return Time.objects.all()

    def get(self, request, *args, **kwargs):
        time = get_object_or_404(self.get_queryset(), id=kwargs.get('time_id'))
        return render(request, self.template_name, {"time": time})


class CoachProfileTimesAthletesPresentationView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get_queryset(self):
        from Classes.models import Time
        return Time.objects.all()

    def get(self, request, *args, **kwargs):
        import jdatetime
        time = get_object_or_404(self.get_queryset(), id=kwargs.get("time_id"))
        presentation = []
        for athlete in time.athletes.all():
            athlete_times = athlete.class_present.filter(date=jdatetime.date.today().togregorian(), user_id=athlete.id,
                                                         is_present=True)
            if athlete_times.exists():
                presentation.append(athlete_times.first().user.id)
        return render(request, self.template_name, {"time": time, "presentation": presentation})

    def post(self, request, *args, **kwargs):
        from Accounts.models import PresentClass
        import jdatetime
        time = get_object_or_404(self.get_queryset(), id=kwargs.get("time_id"))
        user_ids = [int(key.split("id-")[-1]) for key in request.POST.keys() if key.startswith("id-")]
        # We Present Every day and this system is designed for everyday presentation so be careful!
        today_presentations = PresentClass.objects.filter(date=jdatetime.date.today().togregorian(), time_id=time.id)
        if today_presentations.exists():
            for presentation in today_presentations:
                if presentation.user.id in user_ids:
                    presentation.is_present = True
                    presentation.save()
                else:
                    presentation.is_present = False
                    presentation.save()
        else:
            for athlete in time.athletes.all():
                if athlete.id in user_ids:
                    time.class_present.create(user_id=athlete.id, is_present=True)
                else:
                    time.class_present.create(user_id=athlete.id)
        messages.success(request, "تغییرات با موفقیت ثبت شد")
        return redirect("Accounts:coach-profile-times")


class CoachProfileTimeAthleteProfileView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        athlete = get_object_or_404(self.get_queryset(), id=kwargs.get("id"))
        return render(request, self.template_name, {"athlete": athlete})


class CoachProfileAddTimeView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    @staticmethod
    def get_coaches():
        from Coach.models import Coach
        return Coach.objects.all()

    @staticmethod
    def get_class_categories():
        from Classes.models import ClassCategory
        return ClassCategory.objects.all()

    @staticmethod
    def get_class_types():
        from Classes.models import ClassType
        return ClassType.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {"coaches": self.get_coaches(), "class_categories": self.get_class_categories()})

    def post(self, request, *args, **kwargs):
        from Classes.models import Time, ClassCategory
        from Coach.models import Coach
        title = request.POST.get('title')
        place_count = request.POST.get("place_count")
        category = request.POST.get("category")
        coach_id = request.POST.get("coach")
        try:
            place_count = int(place_count)
            if place_count < 0 or place_count > 99:
                raise ValueError
        except ValueError:
            messages.error(request, "لطفا برای ظرفیت یک عدد بین 0 تا 99 انتخاب کنید.")
            return redirect("Accounts:coach-add-time")
        try:
            category_id = int(category)
            category = ClassCategory.objects.get(id=category_id)
        except ValueError:
            messages.error(request, "لطفا دسته بندی مناسب را انتخاب کنید.")
            return redirect("Accounts:coach-add-time")
        except ClassCategory.DoesNotExist:
            messages.error(request, "دسته بندی مورد نظر یافت نشد.")
            return redirect("Accounts:coach-add-time")
        try:
            coach_id = int(coach_id)
            coach = Coach.objects.get(id=coach_id)
        except ValueError:
            messages.error(request, "مربی را به  درستی انتخاب کنید")
            return redirect("Accounts:coach-add-time")
        except Coach.DoesNotExist:
            messages.error(request, "مربی را به  درستی انتخاب کنید")
            return redirect("Accounts:coach-add-time")
        if title is None:
            messages.error(request, "لطفا عنوان کلاس را وارد کنید")
            return redirect("Accounts:coach-add-time")
        Time.objects.create(title=title, place_count=place_count, category=category, coach=coach, class_type_id=1)
        messages.success(request, "افزودن کلاس با موفقیت انجام شد")
        return redirect("Accounts:coach-profile-times")


class CoachProfileClassListView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    @staticmethod
    def get_queryset(slug=None):
        from Classes.models import OnlineClass
        if slug is not None:
            return OnlineClass.objects.filter(category__slug=slug)
        return OnlineClass.objects.all()

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug", None)
        class_categories = CoachProfileAddTimeView.get_class_categories()
        if slug is not None:
            return render(request, self.template_name,
                          {"classes": self.get_queryset(slug=slug), "class_categories": class_categories, "slug": slug})
        return render(request, self.template_name,
                      {"classes": self.get_queryset(), "class_categories": class_categories})


class CoachProfileClassAddCategoryView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        from django.utils.text import slugify
        from Classes.models import ClassCategory
        image = request.FILES.get("image")
        name = request.POST.get("name")
        slug = slugify(request.POST.get("slug"))
        if ClassCategory.objects.filter(slug=slug).exists():
            slug = f"{slug}-{ClassCategory.objects.count() + 1}"
        ClassCategory.objects.create(name=name, slug=slug, image=image)
        messages.success(request, "دسته بندی افزوده شد")
        return redirect("Accounts:coach-class-list")


class CoachProfileClassSelectCategoryView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    def get(self, request):
        return render(request, self.template_name,
                      {"class_categories": CoachProfileClassEditCategoryView.get_queryset()})


class CoachProfileClassEditCategoryView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/coach-profile.html"

    @staticmethod
    def get_queryset():
        from Classes.models import ClassCategory
        return ClassCategory.objects.all()

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        category = get_object_or_404(self.get_queryset(), slug=slug)
        return render(request, self.template_name, {"category": category})

    def post(self, request, *args, **kwargs):
        from django.utils.text import slugify
        from Classes.models import ClassCategory
        category = get_object_or_404(self.get_queryset(), slug=kwargs.get('slug'))
        delete = request.POST.get("delete")
        if delete:
            category.delete()
            messages.info(request, "دسته بندی حذف شد")
            return redirect("Accounts:coach-class-list")
        image = request.FILES.get("image")
        name = request.POST.get("name")
        slug = slugify(request.POST.get("slug"))
        if ClassCategory.objects.filter(slug=slug).exists():
            slug = f"{slug}-{ClassCategory.objects.count() + 1}"
        category.slug = slug
        category.slug = slug
        category.name = name
        if image:
            category.image = image
        category.save()
        messages.success(request, "دسته بندی آپدیت شد")
        return redirect("Accounts:coach-class-list")


class CoachProfileClassAddView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/components/coach_add_class.html"

    @staticmethod
    def get_start_time(date: str):
        import jdatetime
        date = list(map(int, date.split("/")))
        return jdatetime.date(year=date[0], month=date[1], day=date[2]).togregorian()

    def get(self, request, *args, **kwargs):
        class_coaches = CoachProfileAddTimeView.get_coaches()
        class_categories = CoachProfileAddTimeView.get_class_categories()
        class_types = CoachProfileAddTimeView.get_class_types()
        return render(request, self.template_name, {
            "class_coaches": class_coaches,
            "class_categories": class_categories,
            "class_types": class_types,
        })

    def post(self, request, *args, **kwargs):
        from Classes.models import OnlineClass
        data = request.POST
        for item in ["title", "slug", "description"]:
            if item not in data.keys():
                messages.warning(request, "لطفا اطلاعات را با دقت وارد کنید.")
                return redirect("Accounts:coach-class-add")
        if "image" not in request.FILES.keys():
            messages.warning(request, "افزودن تصویر اجباری است!")
            return redirect("Accounts:coach-class-add")
        try:
            title = data.get("title")
            description = data.get("description")
            slug = slugify(data.get("slug"))
            coach_id = int(data.get("class_coach"))
            date = self.get_start_time(data.get("start_date"))
            place_count = int(data.get("place_count"))
            sessions_count = int(data.get("sessions_count"))
            sessions_count_in_week = int(data.get("sessions_count_in_week"))
            sessions_duration = int(data.get("sessions_duration"))
            price = int(data.get("price"))
            category_id = int(data.get("class_category"))
            type_id = int(data.get("class_types"))
        except:
            messages.error(request, "لطفا بار دیگر تلاش کنید")
            return redirect("Accounts:coach-class-add")
        OnlineClass.objects.create(title=title, description=description, slug=slug, start_time=date, coach_id=coach_id,
                                   place_count=place_count, image=request.FILES.get("image"),
                                   sessions_count=sessions_count, sessions_duration=sessions_duration,
                                   sessions_count_in_week=sessions_count_in_week, price=price, category_id=category_id,
                                   class_type_id=type_id)
        messages.success(request, "کلاس با موفقیت ساخته شد")
        return redirect("Accounts:coach-class-list")


class CoachProfileClassEditView(LoginRequiredMixin, IsAdminRequiredMixin, View):
    template_name = "Accounts/components/coach_edit_class.html"

    @staticmethod
    def get_queryset():
        from Classes.models import OnlineClass
        return OnlineClass.objects.all()

    def get(self, request, *args, **kwargs):
        _class = get_object_or_404(self.get_queryset(), slug=kwargs.get("slug"))
        class_coaches = CoachProfileAddTimeView.get_coaches()
        class_categories = CoachProfileAddTimeView.get_class_categories()
        class_types = CoachProfileAddTimeView.get_class_types()
        return render(request, self.template_name, {
            "class": _class,
            "class_coaches": class_coaches,
            'class_categories': class_categories,
            'class_types': class_types
        })

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        _class = get_object_or_404(self.get_queryset(), slug=kwargs.get("slug"))
        try:
            if image is not None:
                _class.image = image
            _class.title = request.POST.get("title")
            _class.slug = slugify(request.POST.get("slug"))
            _class.description = request.POST.get("description")
            _class.coach_id = int(request.POST.get("class_coach"))
            _class.category_id = int(request.POST.get("class_category"))
            _class.class_type_id = int(request.POST.get("class_types"))
            _class.start_time = CoachProfileClassAddView.get_start_time(request.POST.get("start_date"))
            _class.place_count = int(request.POST.get("place_count"))
            _class.sessions_count = int(request.POST.get("sessions_count"))
            _class.sessions_count_in_week = int(request.POST.get("sessions_count_in_week"))
            _class.sessions_duration = int(request.POST.get("sessions_duration"))
            _class.price = int(request.POST.get("price"))
            _class.save()
        except:
            messages.error(request, "خطایی روی داد، لطفا دوباره تلاش کنید.")
            return redirect("Accounts:coach-class-edit", {"slug": _class.slug})
        messages.success(request, "تغییرات با موفقیت اعمال شد")
        return redirect("Accounts:coach-class-list")
