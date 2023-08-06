from django.urls import path
from . import views

app_name = "Classes"
urlpatterns = [
    path("", views.ClassIndexView.as_view(), name="classes_index"),
    path("group_classes/", views.GroupClassListView.as_view(), name="group_classes"),
    path("private_classes/", views.PrivateClassListView.as_view(), name="private_classes"),
    path("category/", views.ClassCategoryView.as_view(), name="classes_category_view"),
    path("category/<slug:slug>/", views.ClassCategoryFilterView.as_view(), name="classes_category_filter"),
    path("group-classes/<slug:slug>/", views.GroupClassView.as_view(), name="group_class_view"),
    path("private-classes/<slug:slug>/", views.PrivateClassView.as_view(), name="private_class_view"),
    path("join-class/<slug:slug>/", views.JoinClassView.as_view(), name="join_class_view"),
    path("join-private-class/<slug:slug>/", views.JoinPrivateClassView.as_view(), name="join_private_class_view"),
]
