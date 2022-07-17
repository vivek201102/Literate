import email
from django.http import JsonResponse
from django.shortcuts import redirect, render
from requests import session
from .models import user

# Create your views here.
def index(request):
    return render(request, "home.html")

def register(request):
    username = request.POST['username']

    user_data = user.objects.filter(username = username).first()
    if user_data is not None:
        return JsonResponse({"message":"Username is already taken"})
    else:
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        user_info = user.objects.create(name = name, email = email, mobile = contact, username = username, password = password)
        user_info.save()
        return JsonResponse({"user":user_info, "message":"user registered successfully"})


def auth(request):
    email = request.POST['email']
    password = request.POST['password']
    user_data = user.objects.filter(email = email, password = password).first()
    if user_data is None:
        print("False")
        return render(request, "signin.html", {"message":"Email or Password is incorrect"})
    else:
        request.session['user_info'] = user_data.email
        return redirect('/')


def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

