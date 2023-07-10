from django.shortcuts import render
from django.views import View
from .models import Coach
from django.shortcuts import get_object_or_404


class CoachIndexView(View):
    template_name = "Coach/index.html"

    def get(self, request):
        coaches = Coach.objects.filter(is_active=True)
        return render(request, self.template_name, {"coaches": coaches})


class CoachDetailView(View):
    template_name = "Coach/coach-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        coach = get_object_or_404(Coach.objects.filter(is_active=True, slug=slug))
        return render(request, self.template_name, {"coach": coach})
