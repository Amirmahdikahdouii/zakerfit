from django.shortcuts import render
from django.views import View
from .models import Coach


class CoachIndexView(View):
    template_name = "Coach/index.html"

    def get(self, request):
        coaches = Coach.objects.filter(is_active=True)
        return render(request, self.template_name, {"coaches": coaches})
