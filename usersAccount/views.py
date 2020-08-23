from django.shortcuts import render
from usersAccount.forms import UserForm,UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,"usersAccount/index.html")

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

            #to store profile picture
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm
        
    return render(request,"usersAccount/signup.html",{'profile_form':profile_form,'user_form':user_form,'registered':registered})