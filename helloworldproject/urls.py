from django.contrib import admin
from django.urls import path

from helloworldproject.views import helloworldfunc

urlpatterns = [
    path("admin/", admin.site.urls),
    path("helloworldurl/", helloworldfunc),
]
