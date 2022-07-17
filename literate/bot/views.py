<<<<<<< HEAD
from email.encoders import encode_7or8bit
from django.http import JsonResponse
from django.shortcuts import redirect, render
from requests import session
import random
from django.db.models import Q
from .models import help, funchat, courses 
# Create your views here.

def check_command(request):
    if request.method == "POST":
        command = request.POST['comd']
        
        list = []
        list = command.split()
        request.POST._mutable = True
        request.POST['command'] = command
        request.POST._mutable = False
        if list[0] == "@start":
            return start_bot(request)
        elif list[0] == "@end":
            return end_bot(request)
        elif list[0] == "@fun":
            return fun_chat(request)
        elif list[0] == "@search":
            return search_content(request)
        elif list[0] == "@help":
            return help_command(request)
        else :
            return JsonResponse({"error":False,"code":0, "instruction":command , "message":"get the help of @help"})
    else: return

def start_bot(request):
    print(request.session['user_info'])
    if request.session['user_info'] == "undefined":
        print("Hello")
        return JsonResponse({"error": False,"code":-1, "message": "User needs to login for using this functionallity"})
    else:
        return JsonResponse({"error": False, "code":5, "message":"Hello", "message1":"Hope you are doing fine. How can I help you?"})
        

def end_bot(request):
    request.session['user_info'] = 'undefined'
    return redirect("/signin")

def fun_chat(request):
    print("Hello")
    comm = request.POST['command']
    command = comm[5:]
    answer_data = funchat.objects.filter(Q(question1__icontains = command) |  Q(question2__icontains = command) | Q(question3__icontains = command) | Q(question4__icontains = command) | Q(question5__icontains = command))
    answer = []

    if answer_data is None:
        return JsonResponse({"error":False,"code":0,"instruction":command ,"message":"Sorry I did not get"})
    else:
        for i in answer_data:
            answer.append(i.answer1)
            answer.append(i.answer2)
            answer.append(i.answer3)
        res = random.choice(answer)
        return JsonResponse({"error":False, "code":3,"instruction":command ,"ans":res}) 

def search_content(request):
    comm = request.POST["command"]
    command = comm[8:]
    answer = []
    answer_data = courses.objects.values().filter(Q(tag1__icontains = command) |  Q(tag2__icontains = command) | Q(tag3__icontains = command))
    if len(answer_data) == 0:
        return JsonResponse({"code":0, "instruction":command , "message":"No courses found as per your requirement"})
    else:
        answer = list(answer_data)
        return JsonResponse({"code":2,"instruction":command ,"message":"data found", "answer": answer})



def help_command(request):
    help_center1 = help.objects.values().all()
    help_center = list(help_center1)
    return JsonResponse({"code":1, "help": help_center})

          
=======
from email.encoders import encode_7or8bit
from django.http import JsonResponse
from django.shortcuts import redirect, render
from requests import session
import random
from django.db.models import Q
from .models import help, funchat, courses 
# Create your views here.

def check_command(request):
    if request.method == "POST":
        command = request.POST['comd']
        
        list = []
        list = command.split()
        request.POST._mutable = True
        request.POST['command'] = command
        request.POST._mutable = False
        if list[0] == "@start":
            return start_bot(request)
        elif list[0] == "@end":
            return end_bot(request)
        elif list[0] == "@fun":
            return fun_chat(request)
        elif list[0] == "@search":
            return search_content(request)
        elif list[0] == "@help":
            return help_command(request)
        else :
            return JsonResponse({"error":False,"code":0, "instruction":command , "message":"get the help of @help"})
    else: return

def start_bot(request):
    print(request.session['user_info'])
    if request.session['user_info'] == "undefined":
        print("Hello")
        return JsonResponse({"error": False,"code":-1, "message": "User needs to login for using this functionallity"})
    else:
        return JsonResponse({"error": False, "code":5, "message":"Hello", "message1":"Hope you are doing fine. How can I help you?"})
        

def end_bot(request):
    request.session['user_info'] = 'undefined'
    return redirect("/signin")

def fun_chat(request):
    print("Hello")
    comm = request.POST['command']
    command = comm[5:]
    answer_data = funchat.objects.filter(Q(question1__icontains = command) |  Q(question2__icontains = command) | Q(question3__icontains = command) | Q(question4__icontains = command) | Q(question5__icontains = command))
    answer = []

    if answer_data is None:
        return JsonResponse({"error":False,"code":0,"instruction":command ,"message":"Sorry I did not get"})
    else:
        for i in answer_data:
            answer.append(i.answer1)
            answer.append(i.answer2)
            answer.append(i.answer3)
        res = random.choice(answer)
        return JsonResponse({"error":False, "code":3,"instruction":command ,"ans":res}) 

def search_content(request):
    comm = request.POST["command"]
    command = comm[8:]
    answer = []
    answer_data = courses.objects.values().filter(Q(tag1__icontains = command) |  Q(tag2__icontains = command) | Q(tag3__icontains = command))
    if len(answer_data) == 0:
        return JsonResponse({"code":0, "instruction":command , "message":"No courses found as per your requirement"})
    else:
        answer = list(answer_data)
        return JsonResponse({"code":2,"instruction":command ,"message":"data found", "answer": answer})



def help_command(request):
    help_center1 = help.objects.values().all()
    help_center = list(help_center1)
    return JsonResponse({"code":1, "help": help_center})

          
          
      
>>>>>>> acc2caff240fd0cc1f6cd8a7d9d7051ec5d3df6b
