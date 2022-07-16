from email.encoders import encode_7or8bit
from django.http import JsonResponse
from django.shortcuts import redirect, render
from requests import session
import random
from django.db.models import Q
from .models import help, funchat, courses 
# Create your views here.

def check_command(request):
    command = request.POST['command']
    list = []
    list = command.split()
    request.POST._mutable = True
    request.POST['command'] = command
    request.POST._mutable = False
    if list[0] == "@start":
        return start_bot
    elif list[0] == "@end":
        return end_bot 
    elif list[0] == "@fun":
        return fun_chat
    elif list[0] == "@search":
        return search_content
    elif list[0] == "@help":
        return help_command
    else :
        return JsonResponse({"message":"get the help of @help"})

def start_bot(request):
    if session['auth'] is None:
        return JsonResponse({"message": "User needs to login for using this functionallity"})
    else:
        return JsonResponse({"message":"Hello", "message1":"Hope you are doing fine. How can I help you?"})
        

def end_bot(request):
    return redirect("/")

def fun_chat(request):
    comm = request.POST['command']
    command = comm[5,]
    answer_data = funchat.objects.filter(Q(question1__icontains = command) |  Q(question2__icontains = command) | Q(question3__icontains = command) | Q(question4__icontains = command) | Q(question5__icontains = command))
    answer = []

    if answer_data is None:
        return JsonResponse({"ans":"Sorry I did not get"})
    else:
        for i in answer_data:
            answer.append(i.answer1)
            answer.append(i.answer2)
            answer.append(i.answer3)
        res = random.choice(answer)
        return JsonResponse({"ans":res}) 

def search_content(request):
    comm = request.POST[command]
    command = comm[7,]
    answer = []
    answer_data = courses.objects.filter(Q(tag1__icontains = command) |  Q(tag2__icontains = command) | Q(tag3__icontains = command))
    if answer_data is None:
        return JsonResponse({"message":"No courses found as per your requirement"})
    else:
        for i in answer_data:
            answer.append(i)
        
        return JsonResponse({"message":"data found", "answer": answer})



    return

def help_command(request):
    help_center = help.objects.all()
    return JsonResponse({"help": help_center})

          
          
      