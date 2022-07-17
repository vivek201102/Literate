from django.http import JsonResponse
from django.shortcuts import render
from .models import book
# Create your views here.
def register(request):
    name = request.POST['name']
    author = request.POST['author']
    publisher = request.POST['publisher']
    price = request.POST['price']
    subject = request.POST['subject']
    user = request.session['user']
    img = request.FILES['pic']
    book_info = book.objects.create(name = name, author = author, publisher = publisher, price = price, subject = subject, user = user, status = 'unsold', image = img)
    book_info.save()
    return JsonResponse({"message":"Book Added successfully", "data":book_info})

def remove(request):
    id = request.POST['id']
    book_info = book.objects.filter(id = id).first()
    book_info.delete()


def change_status(request):
    id = request.POST['id']
    book_info = book.objects.filter(id = id).update(status = 'sold')