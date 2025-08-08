from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is the home page ")

def about(request):
    return HttpResponse("This is the about page ")

def contact(request):
    return HttpResponse("This is the contact page ")