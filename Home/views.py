from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "Home/index.html"

    def get(self, request):
        from Classes.models import Time
        week_days = ["شنبه", "یک شنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه"]
        return render(request, self.template_name, {"class_times": Time.objects.all(), "week_days": week_days})
