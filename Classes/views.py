from django.shortcuts import render
from django.views import View
from .models import GroupOnlineClass, PrivateOnlineClass
from django.shortcuts import get_object_or_404


class ClassIndexView(View):
    template_name = "Classes/index.html"

    def get(self, request, *args, **kwargs):
        group_online_classes = GroupOnlineClass.objects.filter(is_active=True).order_by("-id")
        private_online_classes = PrivateOnlineClass.objects.filter(is_active=True).order_by("-id")
        return render(request, self.template_name, {
            "classes": list(private_online_classes) + list(group_online_classes),
        })


class GroupClassListView(View):
    template_name = "Classes/index.html"

    def get(self, request):
        group_online_classes = GroupOnlineClass.objects.filter(is_active=True).order_by("-id")
        return render(request, self.template_name, {
            "classes": group_online_classes,
        })


class PrivateClassListView(View):
    template_name = "Classes/index.html"

    def get(self, request):
        private_online_classes = PrivateOnlineClass.objects.filter(is_active=True).order_by("-id")
        return render(request, self.template_name, {
            "classes": private_online_classes,
        })


class GroupClassView(View):
    template_name = "Classes/class-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        queryset = get_object_or_404(GroupOnlineClass.objects.filter(is_active=True), slug=slug)
        return render(request, self.template_name, {"class": queryset})


class PrivateClassView(View):
    template_name = "Classes/class-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        queryset = get_object_or_404(PrivateOnlineClass.objects.filter(is_active=True), slug=slug)
        return render(request, self.template_name, {"class": queryset})
