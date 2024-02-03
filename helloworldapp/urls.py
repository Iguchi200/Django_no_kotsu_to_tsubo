from django.urls import path

from helloworldapp.views import helloworldfunc

urlpatterns = [
    path("helloworldapp/", helloworldfunc),
]
