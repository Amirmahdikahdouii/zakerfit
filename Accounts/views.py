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
