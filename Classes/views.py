from django.shortcuts import render
from django.views import View
from .models import OnlineClass
from django.shortcuts import get_object_or_404


class ClassIndexView(View):
    template_name = "Classes/index.html"

    def get(self, request, *args, **kwargs):
        classes = OnlineClass.objects.filter(is_active=True).order_by("-id")
        return render(request, self.template_name, {
            "classes": classes,
        })


class GroupClassListView(View):
    template_name = "Classes/index.html"

    def get(self, request):
        group_online_classes = OnlineClass.objects.filter(is_active=True, class_type__class_type=2).order_by("-id")
        return render(request, self.template_name, {
            "classes": group_online_classes,
        })


class PrivateClassListView(View):
    template_name = "Classes/index.html"

    def get(self, request):
        private_online_classes = OnlineClass.objects.filter(is_active=True, class_type__class_type=3).order_by("-id")
        return render(request, self.template_name, {
            "classes": private_online_classes,
        })


class GroupClassView(View):
    template_name = "Classes/class-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        queryset = get_object_or_404(OnlineClass.objects.filter(is_active=True, class_type__class_type=2), slug=slug)
        return render(request, self.template_name, {"class": queryset})


class PrivateClassView(View):
    template_name = "Classes/class-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        queryset = get_object_or_404(OnlineClass.objects.filter(is_active=True, class_type__class_type=3), slug=slug)
        return render(request, self.template_name, {"class": queryset})
