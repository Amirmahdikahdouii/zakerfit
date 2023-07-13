from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.views import View
from .models import User
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


class SignUpView(View):
    template_name = "Accounts/forms.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("Home:home_view")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": SignUpForm()})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get("phone_number")
            if User.objects.filter(phone_number=phone_number).exists():
                messages.error(request, "این شماره همراه قبلا در سیستم ثبت شده است")
                return redirect("Accounts:sign-up")
            password = form.cleaned_data.get("password")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            User.objects.create_user(phone_number=phone_number, password=password,
                                     **{"first_name": first_name, "last_name": last_name})
            return redirect("Home:home_view")
        for error in form.errors:
            if error == "password":
                messages.error(request,
                               message="پسورد باید حداقل 8 کاراکتر باشد و متشکل از حروف یا حروف و اعداد و کاراکتر باشد.")
            elif error == "confirm_password":
                messages.error(request, message="پسورد ها باید با همدیگر یکسان باشند")
            else:
                messages.error(request, message="مشکلی پیش آمد، لطفا بعدا تلاش کنید.")
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    template_name = "Accounts/forms.html"
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("Home:home_view")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get("phone_number")
            password = form.cleaned_data.get("password")
            try:
                User.objects.get(phone_number=phone_number)
                user = authenticate(request, phone_number=phone_number, password=password)
                if user is None:
                    raise User.DoesNotExist
                messages.success(request, "با موفقیت وارد شدید")
                login(request, user)
                return redirect("Accounts:profile")
            except User.DoesNotExist:
                messages.error(request, "شماره همراه یافت نشد")
                return redirect("Accounts:login")
        messages.error(request, "لطفا اطلاعات را با دقت وارد کنید")
        return redirect("Accounts:login")


class LogOutView(LogoutView):
    next_page = "/"

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "با موفقیت خارج شدید")
        return super(LogOutView, self).dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, View):
    login_url = "/Accounts/login/"
    template_name = "Accounts/profile.html"

    def get(self, request):
        return render(request, self.template_name)


@method_decorator(csrf_exempt, name="dispatch")
class ChangeUserBirthdayView(LoginRequiredMixin, View):
    login_url = "/Accounts/login"

    def post(self, request, *args, **kwargs):
        import json
        import jdatetime
        data = json.loads(request.body)
        date = list(map(int, data.get("date").split("/")))
        request.user.birthday = jdatetime.date(year=date[0], month=date[1], day=date[2]).togregorian()
        request.user.save()
        return HttpResponse(status=200)


@method_decorator(csrf_exempt, "dispatch")
class ChangeUserGenderView(LoginRequiredMixin, View):
    login_url = "/Accounts/login"

    def post(self, request):
        request.user.gender = 1 if request.user.gender == 2 else 2
        request.user.save()
        return JsonResponse(data={"gender": request.user.gender}, status=200)


class ChangeUserProfileView(LoginRequiredMixin, View):
    login_url = "/Accounts/login"

    def post(self, request):
        request.user.profile_image = request.FILES["profile_image"]
        request.user.save()
        messages.success(request, "تصویر پروفایل با موفقیت تغییر کرد.")
        return redirect("Accounts:profile")


class RegisterPresentClassView(LoginRequiredMixin, View):
    template_name = "Accounts/register_present_class.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.class_time is not None:
            messages.warning(request, "شما از قبل در کلاسی حضور دارید، برای تغییر زمان بندی از پروفایل خود اقدام کنید.")
            return redirect("Accounts:profile")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        from Classes.models import Time
        time_id = kwargs.get("id")
        if time_id is not None:
            time = get_object_or_404(Time.objects.all(), id=time_id)
            request.user.class_time = time
            request.user.save()
            time.athlete_count += 1
            if time.athlete_count == time.place_count:
                time.has_place_remain = False
            time.save()
            messages.success(request, f"تایم {time.title} برای شما انتخاب شد. ")
            return redirect("Accounts:profile")
        class_times = Time.objects.all()
        week_days = ["شنبه", "یک شنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "انتخاب کلاس"]
        return render(request, self.template_name, {
            "class_times": class_times,
            "week_days": week_days
        })


class ChangePresentClassView(LoginRequiredMixin, View):
    template_name = "Accounts/change_present_class_time.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.class_time is None:
            messages.warning(request,
                             "شما در کلاسی ثبت نام نکرده اید، برای ثبت نام در کلاس از پروفایل خودتون اقدام کنین!")
            return redirect("Accounts:profile")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        from Classes.models import Time
        new_time_id = kwargs.get("id")
        if new_time_id is not None:
            new_time = get_object_or_404(Time.objects.filter(has_place_remain=True), id=new_time_id)
            old_time = request.user.class_time
            old_time.athlete_count -= 1
            if old_time.athlete_count < old_time.place_count and old_time.has_place_remain:
                old_time.has_place_remain = True
            old_time.save()
            new_time.athlete_count += 1
            if new_time.athlete_count == new_time.place_count:
                new_time.has_place_remain = False
            new_time.save()
            request.user.class_time = new_time
            request.user.save()
            messages.success(request, f"تایم شما به {new_time.title} تغییر کرد")
            return redirect("Accounts:profile")
        class_times = Time.objects.filter(has_place_remain=True)
        class_times = [time for time in class_times if time.id != request.user.class_time_id]
        return render(request, self.template_name, {"class_times": class_times})
