from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    [
      path("accounts/", include("django.contrib.auth.urls")),
      path("reviewpost/", include("reviewpost.urls")),
      path("blogpost/", include("blogpost.urls")),
      path("reviewpost/", include("reviewpost.urls")),
      path("admin/", admin.site.urls),
      path("", include("helloworldapp.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
