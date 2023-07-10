from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("Accounts/", include("Accounts.urls", namespace="Accounts")),
                  path("Classes/", include("Classes.urls", namespace="Classes")),
                  path("Coaches/", include("Coach.urls", namespace="Coaches")),
                  path("", include("Home.urls", namespace="Home")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
