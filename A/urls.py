from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Accounts/", include("Accounts.urls", namespace="Accounts")),
    path("", include("Home.urls", namespace="Home")),
]
