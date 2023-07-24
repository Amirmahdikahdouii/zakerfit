from django.shortcuts import render, redirect
from Accounts.forms import SignUpForm, LoginForm
from django.views import View
from Accounts.models import User
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
            messages.success(request, "حساب کاربری شما با موفقیت ساخته شد، اکنون وارد شوید")
            return redirect("Accounts:profile")
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
                if request.user.phone_validation.is_verify is False:
                    return redirect("Accounts:verify_phone_number_view")
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.phone_validation.is_verify is False:
            messages.warning(request, "لطفا ابتدا شماره همراه خودتون رو تایید کنید.")
            return redirect("Accounts:verify_phone_number_view")
        return super().dispatch(request, *args, **kwargs)

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
        from Accounts.models import UserTimePayment
        import jdatetime
        if request.user.is_authenticated and request.user.class_time is not None:
            messages.warning(request, "شما از قبل در کلاسی حضور دارید، برای تغییر زمان بندی از پروفایل خود اقدام کنید.")
            return redirect("Accounts:profile")
        user_payment = UserTimePayment.objects.filter(user_id=request.user.id).order_by("-date").first()
        if user_payment.sessions_remain == 0:
            messages.error(request, "تعداد جلسات شما به پایان رسیده است، لطفا پلن خود را انتخاب کنید.")
            return redirect("Accounts:time_payment_form")
        date_difference = jdatetime.date.today() - user_payment.date
        if date_difference.days > 35:
            messages.error(request, "مدت زمان پلن انتخابی شما به پایان رسیده است، لطفا پلن خود را شارژ کنید")
            return redirect("Accounts:time_payment_form")
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


@method_decorator(csrf_exempt, "dispatch")
class VerifyPhoneNumberView(LoginRequiredMixin, View):
    template_name = "Accounts/verify_phone_number.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.phone_validation.is_verify:
            messages.success(request, "شماره همراه شما قبلا تایید شده است.")
            return redirect("Accounts:profile")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        import json
        data = json.loads(request.body)
        code = data.get("code")
        if code == request.user.phone_validation.code:
            request.user.phone_validation.is_verify = True
            request.user.phone_validation.save()
            return HttpResponse(status=200)
        return HttpResponse(status=403)


class DeletePresentClassView(LoginRequiredMixin, View):
    def get(self, request):
        request.user.class_time.athlete_count -= 1
        if request.user.class_time.has_place_remain is False:
            request.user.class_time.has_place_remain = True
        request.user.class_time.save()
        request.user.class_time = None
        request.user.save()
        messages.success(request, "کلاس شما با موفقیت حذف شد")
        return redirect("Accounts:profile")


class TimePaymentView(LoginRequiredMixin, View):
    template_name = "Accounts/time_payment_form.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, " لطفا ابتدا وارد شوید!")
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def get_time_plans():
        from Classes.models import TimePrice
        return TimePrice.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "time_prices": self.get_time_plans(),
        })

    def post(self, request, *args, **kwargs):
        # TODO: Fix Payment section and make real connection to payment server
        from Accounts.models import UserTimePayment
        try:
            time_price_id = int(request.POST.get("time_plan"))
            time_price = get_object_or_404(self.get_time_plans(), id=time_price_id)
        except ValueError:
            messages.error(request, "لطفا اطلاعات را به درستی وارد کنید")
            return redirect("Accounts:time_payment_form")
        UserTimePayment.objects.create(user_id=request.user.id, time_pricing=time_price,
                                       sessions_remain=time_price.sessions_count)
        return redirect("Accounts:time_payment_confirm")


class TimePaymentConfirmView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # TODO: Confirm Payment Status, by default now is True
        messages.success(request, "پرداخت با موفقیت انجام شد، خوشحالیم که کنارمون هستین!")
        return redirect("Accounts:register_present_class")
