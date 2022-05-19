from msilib.schema import InstallUISequence
from pickle import FALSE
from django.db.models import Q
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileEditForm, SkillForm
from django.contrib.auth.decorators import login_required
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
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    #profiles = Profile.objects.filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query))
    skills = Skill.objects.filter(
        Q(name__icontains=search_query)
    )
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    context = {'profiles' : profiles, 'search_query':search_query}
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
            return redirect('edit-profile')
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

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/edit_profile.html', context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            skill.save()
            messages.success(request, 'Skill Updated Successfully!!')
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)  

    if request.method == 'POST':
        #skill = SkillForm(request.POST, instance=skill)
        skill = profile.skill_set.get(id=pk)
        skill.delete()
        messages.success(request, 'Deleted Successfully !!')
        return redirect('account')

    context = {'object':skill, 'back':'account', 'type':'Skill'}
    return render(request, 'delete_template.html', context)