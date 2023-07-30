from django.shortcuts import render
from django.views import View
from .models import OnlineClass, ClassCategory
from django.shortcuts import get_object_or_404, get_list_or_404


class Utilities:
    @staticmethod
    def get_class_categories():
        return ClassCategory.objects.all()


class ClassIndexView(View):
    template_name = "Classes/index.html"

    def get(self, request, *args, **kwargs):
        classes = OnlineClass.objects.filter(is_active=True).order_by("-id")
        return render(request, self.template_name, {
            "classes": classes,
            'class_categories': Utilities.get_class_categories(),
        })


class GroupClassListView(View):
    template_name = "Classes/index.html"

    def get(self, request):
        group_online_classes = OnlineClass.objects.filter(is_active=True, class_type__class_type=2).order_by("-id")
        return render(request, self.template_name, {
            "classes": group_online_classes,
            'class_categories': Utilities.get_class_categories(),
        })


class PrivateClassListView(View):
    template_name = "Classes/index.html"

    def get(self, request):
        private_online_classes = OnlineClass.objects.filter(is_active=True, class_type__class_type=3).order_by("-id")
        return render(request, self.template_name, {
            "classes": private_online_classes,
            'class_categories': Utilities.get_class_categories(),
        })


class GroupClassView(View):
    template_name = "Classes/class-detail.html"

    @staticmethod
    def get_class_categories():
        from .models import ClassCategory
        return ClassCategory.objects.all()

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        queryset = get_object_or_404(OnlineClass.objects.filter(is_active=True, class_type__class_type=2), slug=slug)
        return render(request, self.template_name, {
            "class": queryset,
            "class_categories": self.get_class_categories(),
        })


class PrivateClassView(View):
    template_name = "Classes/class-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        queryset = get_object_or_404(OnlineClass.objects.filter(is_active=True, class_type__class_type=3), slug=slug)
        return render(request, self.template_name, {
            "class": queryset,
            "class_categories": GroupClassView.get_class_categories(),
        })


class ClassCategoryView(View):
    template_name = "Classes/category_index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "class_categories": Utilities.get_class_categories(),
        })


class ClassCategoryFilterView(View):
    template_name = "Classes/index.html"

    @staticmethod
    def get_queryset():
        return OnlineClass.objects.all()

    def get(self, request, *args, **kwargs):
        classes = self.get_queryset().filter(category__slug=kwargs.get("slug"))
        return render(request, self.template_name, {
            "classes": classes,
            'class_categories': Utilities.get_class_categories(),
        })
