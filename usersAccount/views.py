from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"usersAccount/index.html")

def signUp(request):
    return render(request,"usersAccount/signup.html")