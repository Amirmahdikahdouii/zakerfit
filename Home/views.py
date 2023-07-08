from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "Home/index.html"

    def get(self, request):
        from Classes.models import Time
        from Coach.models import Coach
        week_days = ["شنبه", "یک شنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه"]
        coaches = Coach.objects.all()
        return render(request, self.template_name, {
            "class_times": Time.objects.all(),
            "week_days": week_days,
            "coaches": coaches
        })
