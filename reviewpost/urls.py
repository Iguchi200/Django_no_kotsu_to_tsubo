from django.urls import path

from reviewpost.views import signupview, loginview, listview, detailview, CreateClass

urlpatterns = (
  [
    path("signup/", signupview, name="signup"),
    path("login/", loginview, name="login"),
    path("list/", listview, name="list"),
    path("detail/<int:pk>/", detailview, name="detail"),
    path("create/", CreateClass.as_view(), name="carate"),
  ]
)
