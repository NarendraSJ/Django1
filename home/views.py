from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    context = {
        'message': 'Hello, this is the home page!'  ,
        'message2': 'This is the second message',
    }
    # return HttpResponse("Hello, this is the home page ")
    return render(request,'index.html')

def about(request): 
    message="This is Super Star Narendra $$"
    return HttpResponse("This is the about page "+message)

def contact(request):
    return HttpResponse("This is the contact page ")