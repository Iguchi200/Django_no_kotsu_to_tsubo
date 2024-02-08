from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from reviewpost.models import ReviewModel

def signupview(request):
  if request.method == "POST":
    username_data = request.POST["username_data"]
    password_data = request.POST["password_data"]
    try:
      user = User.objects.create_user(username_data, "", password_data)
    except IntegrityError:
      return render(request, "signup.html", {"error": "このユーザーはすでに登録されています"})
  else:
    print(User.objects.all())
    # return render(request, "signup.html", {})
  return render(request, "signup.html", {})

def loginview(request):
  if request.method == "POST":
    username_data = request.POST["username_data"]
    password_data = request.POST["password_data"]
    user = authenticate(request, username=username_data, password=password_data)
    if user is not None:
      login(request, user)
      return redirect("list")
    else:
      return redirect("login")
  return render(request, "login.html", {})

def listview(request):
  object_list = ReviewModel.objects.all()
  return render(request, "list.html", {"object_list": object_list})
