from django.urls import path

from reviewpost.views import signupview

urlpatterns = [
  path("signup/", signupview, name="signup"),
]
