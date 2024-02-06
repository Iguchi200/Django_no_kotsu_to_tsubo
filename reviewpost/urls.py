from django.urls import path

from reviewpost.views import signupview, loginview

urlpatterns = [
  path("signup/", signupview, name="signup"),
  path("login/", loginview, name="login"),
]
