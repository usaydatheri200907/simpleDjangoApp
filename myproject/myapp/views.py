from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")

def hello_view(request):
    return HttpResponse("Hello, world!")
