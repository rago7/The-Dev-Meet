from pickle import FALSE
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated: # if the user is already login nd tries to access login page , this will redirect them to Profiles page
        return redirect('profiles')

    if request.method == 'POST':
        #print(request.POST)
        page = 'login'
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
    context = {'page':page}
    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User logged-out Successfully!!')
    return redirect('login')

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=FALSE)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Signup Successful !!')

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An Error Occurred During Registration :(')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    projects = profile.project_set.all()
    context = {'profile' : profile, 'topSkills':topSkills, 'otherSkills':otherSkills, 'projects':projects}
    return render(request, 'users/user-profile.html', context)
