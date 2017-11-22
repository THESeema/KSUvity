from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from KSUvity.authentication.forms import SignUpForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from KSUvity.models import Activity
from KSUvity.models import Attendee
from .forms import ActivityForm


@login_required
def home(request):
    return render(request, 'student.html')


#def dashboard(request):
#    return render(request, 'dashboard.html')


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

#def admin(request):
 #   return render(request, 'admin.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
             user = User.objects.create_user(
                                              username=email,
                                              email=email,
                                              password=pass_1,
                                              first_name=firstname,
                                              last_name=lastname,

                                            )
             
             
             login(request, user)
             return redirect('home')
        else:
             error = " Password Mismatch "
             return render(request, 'signup.html',{"error":error})
    else:
         return render(request, 'signup.html')

def Login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
   
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            if user.is_superuser:
                 login(request, user)
                 return redirect('admin')
            else:
                 login(request, user)
                 return redirect('home')
        else:
            error = " Sorry! Email and Password didn't match, Please try again ! "
            return render(request, 'login.html',{'error':error})
    else:
        return render(request, 'login.html')

def admin(request):
    data=Activity.objects.all()
    return render(request, 'admin.html', {"data": data})

def post_new(request):
 form = ActivityForm(request.POST)
 if form.is_valid():
    new_activity = form.save()

def dashboard(request):
    data=Activity.objects.all()
    return render(request, 'dashboard.html', {"data": data})

def registerAttende(request,pk):
    act = Activity.objects.get(pk=pk)
    act.save()
    attendee, _ = Attendee.objects.get_or_create(student=request.user)
    act.attendee.add(attendee)
    return render(request, 'dashboard.html')

def home2(request):
    data=Attendee.objects.get(student=request.user)
    return render(request, 'student.html', {"data": data})
