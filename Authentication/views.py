from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, HttpResponseRedirect
from .forms import signupForm, updateProfileForm, updateAdminProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account created successfully!!")
            fm = signupForm()
    else:
        fm = signupForm()
    return render(request, 'enroll/signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully!!")
                    return HttpResponseRedirect('/message')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/message/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = updateAdminProfileForm(
                    data=request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = updateProfileForm(
                    data=request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile Updated!!")
        else:
            if request.user.is_superuser == True:
                fm = updateAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = updateProfileForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password Changed successfully")
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def user_detail(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        fm = updateAdminProfileForm(instance=user)
        return render(request, 'enroll/userdetail.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def home(request):
    return render(request, 'enroll/home.html')
