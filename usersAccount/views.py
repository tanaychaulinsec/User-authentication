from django.shortcuts import render, redirect
from usersAccount.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "usersAccount/index.html")

@login_required
def profile(request):
    return render(request,"usersAccount/profile.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def signup(request):
    
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
    
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            # hashing the password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            #oneToOne relation with User models
            profile.user = user
            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm
        
    return render(request, "usersAccount/signup.html", {'profile_form': profile_form, 'user_form': user_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page like profile page
                return redirect('profile')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'usersAccount/login.html', {})