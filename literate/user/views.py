from django.http import JsonResponse
from django.shortcuts import render
from requests import session
from .models import user

# Create your views here.
def index(request):
    return render(request, "home.html")

def create(request):
    username = request.POST['username']

    user_data = user.objects.filter(username = username).first()
    if user_data is None:
        return JsonResponse({"message":"Username is already taken"})
    else:
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        user_info = user.objects.create(name = name, email = email, contact = contact, username = username, password = password)
        user_info.save()
        return JsonResponse({"user":user_info, "message":"user registered successfully"})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user_data = user.objects.filter(username = username, password = password)
    if user_data is None:
        return JsonResponse({"message":"User not verified"})
    else:
        session['auth'] = user_data
        return JsonResponse({"message":"User varified"})


