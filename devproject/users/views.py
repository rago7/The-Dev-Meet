from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def loginUser(request):

    if request.user.is_authenticated: # if the user is already login nd tries to access login page , this will redirect them to Profiles page
        return redirect('profiles')

    if request.method == 'POST':
        #print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User name Does not Exist')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is Incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User logged-out Successfully!!')
    return redirect('login')

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    projects = profile.project_set.all()
    context = {'profile' : profile, 'topSkills':topSkills, 'otherSkills':otherSkills, 'projects':projects}
    return render(request, 'users/user-profile.html', context)
