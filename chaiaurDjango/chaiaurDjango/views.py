from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at chat aur Django Home page")
    return render(request,'website/index.html')

def about(request):
    # return HttpResponse("Hello, world. You are at chat aur Django About page")
    return render(request,'website/about.html')

def contact(request):
    # return HttpResponse("Hello, world. You are at chat aur Django Contact page") 
    return render(request,'website/contact.html')