from django.urls import path

from reviewpost.views import signupview, loginview, listview, detailview

urlpatterns = (
  [
    path("signup/", signupview, name="signup"),
    path("login/", loginview, name="login"),
    path("list/", listview, name="list"),
    path("detail/<int:pk>/", detailview, name="detail"),
  ]
)
