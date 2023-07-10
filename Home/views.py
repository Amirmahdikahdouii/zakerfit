from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "Home/index.html"

    def get(self, request):
        from Classes.models import Time, OnlineClass
        from Coach.models import Coach
        week_days = ["شنبه", "یک شنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه"]
        coaches = Coach.objects.all()
        online_classes = list(OnlineClass.objects.filter(is_active=True).order_by("-id")[:5])
        return render(request, self.template_name, {
            "online_classes": online_classes,
            "class_times": Time.objects.all(),
            "week_days": week_days,
            "coaches": coaches
        })
