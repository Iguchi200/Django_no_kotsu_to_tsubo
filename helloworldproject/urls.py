from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path("admin/", admin.site.urls),
  path("reviewpost/", include("reviewpost.urls")),
  path("blogpost/", include("blogpost.urls")),
  path("reviewpost/", include("reviewpost.urls")),
  path("", include("helloworldapp.urls")),
]
