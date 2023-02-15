from .forms import UpdateStudHealthForm
from .models import Student
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def update_health_view(request):
    if not request.user.is_authenticated:
        return "///"

    if not Student.objects.filter(user = request.user).exists():
        student = Student()
    else:
        student = Student.objects.get(user = request.user)
    
    if request.method == 'POST':
        update_health_form = request.POST
        student.user = request.user
        student.aadhar = update_health_form.get('aadhar') or student.aadhar
        student.admission_no = update_health_form.get('admission_no') or student.admission_no
        student.name = update_health_form.get('name') or student.name
        student.sex = update_health_form.get('sex') or student.sex
        student.bloodgrp = update_health_form.get('bloodgrp') or student.bloodgrp
        student.birthdate = update_health_form.get('birthdate') or student.birthdate
        student.parent_guardian = update_health_form.get('parent_guardian') or student.parent_guardian
        student.stud_class = update_health_form.get('stud_class') or student.stud_class
        student.height = update_health_form.get('height') or student.height
        student.weight = update_health_form.get('weight') or student.weight
        student.save()
        return render(request, 'update_health.html')

    update_health_form = UpdateStudHealthForm()
    return render(request, 'update_health.html', {'update_health_form': update_health_form})


def home(request):
    return render(request, 'student.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('student:home')

    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('student:home')
    elif request.method == "GET":
        login_form = AuthenticationForm()
        return render(request, 'stud_log.html', {'login_form': login_form})
    
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('student:home')
    
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        print(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            return redirect('student:login')
    else:
        signup_form = UserCreationForm()
    
    return render(request, 'reg_student.html', {'signup_form': signup_form})

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('student:login')
    logout(request)
    return redirect('student:login')