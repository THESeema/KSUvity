from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from KSUvity.authentication.forms import SignUpForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from KSUvity.models import Activity
from KSUvity.models import Attendee
from KSUvity.models import Volunteer

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render_to_response

import datetime
from django.utils import timezone


@login_required
def home(request):
    attendee = Attendee.objects.filter(student=request.user)
    volunteer = Volunteer.objects.filter(student=request.user)
    today = datetime.datetime.today()
    tomorrow = timezone.now() + datetime.timedelta(days=1)


    upcomingAsAttendee=Activity.objects.filter(attendee=attendee , startDate__gte=today)
    upcomingAsVolunteer=Activity.objects.filter(volunteer=volunteer, startDate__gte=today)

    HistoryOfAttendance=Activity.objects.filter(attendee=attendee, endDate__lt=today)
    HistoryOfVolunteer=Activity.objects.filter(volunteer=volunteer, endDate__lt=today)

    for x in upcomingAsAttendee:
        if x.startDate.date() == tomorrow.date():
            messages.warning(request, 'REMINDER: You have the '+x.title+' activity coming up tomorrow!', extra_tags='alert')

    for y in upcomingAsVolunteer:
        if y.startDate.date() == tomorrow.date():
            messages.warning(request, 'REMINDER: You have the '+y.title+' activity coming up tomorrow!', extra_tags='alert')

    return render(request, 'student.html', {"HistoryOfAttendance": HistoryOfAttendance , "HistoryOfVolunteer": HistoryOfVolunteer , "upcomingAsAttendee": upcomingAsAttendee , "upcomingAsVolunteer": upcomingAsVolunteer , "tomorrow" : tomorrow})

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
    today = datetime.datetime.today()

    upcoming=Activity.objects.filter(owner=request.user , startDate__gte=today)
    history=Activity.objects.filter(owner=request.user, endDate__lt=today)

    return render(request, 'admin.html', {"upcoming": upcoming , "history": history})
    
#def checkUserAttendee(request,pk):
#    act = Activity.objects.get(pk=pk)
#    act.save()
#    attendee = Attendee.objects.get(student=request.user)
 #   return render(request, 'dashboard.html', {"data2": data2})

def dashboard(request):
    today = datetime.datetime.today()
    data=Activity.objects.all().exclude(startDate__lt=today)
    return render(request, 'dashboard.html', {"data": data})

def registerAttendee(request,pk):
    act = Activity.objects.get(pk=pk)
    act.save()
    attendee, _ = Attendee.objects.get_or_create(student=request.user)

    volunteer = Volunteer.objects.filter(student=request.user)

    ActvsStudentAttending=Activity.objects.filter(attendee=attendee)
    ActvsStudentVolunteering=Activity.objects.filter(volunteer=volunteer)

    if act.volunteer.filter(student=request.user).exists():
        messages.error(request, 'You\'re already registered as a volunteer for this activity!', extra_tags='alert')
        return redirect('home/#work')
    elif act.attendee.filter(student=request.user).exists():
        messages.warning(request, 'You\'re already registered as an attendee for this activity!', extra_tags='alert')
        return redirect('home/#work')

    elif ActvsStudentAttending.exists():
        for x in ActvsStudentAttending:
            if x.startDate.date() == act.startDate.date():
                messages.error(request, 'You\'re already registered in the '+x.title+' activity that is held on the same day as '+act.title+'!', extra_tags='alert')
                return redirect('home/#work')

    elif ActvsStudentVolunteering.exists():
        for x in ActvsStudentVolunteering:
            if x.startDate.date() == act.startDate.date():
                messages.error(request, 'You\'re already registered in the '+x.title+' activity that is held on the same day as '+act.title+'!', extra_tags='alert')
                return redirect('home/#work')
    else:
        act.attendee.add(attendee)
        messages.success(request, 'You\'re successfully registered as an attendee!', extra_tags='alert')
        return redirect('home/#work')


def registerVolunteer(request,pk):
    act = Activity.objects.get(pk=pk)
    act.save()
    volunteer, _ = Volunteer.objects.get_or_create(student=request.user)

    attendee = Attendee.objects.filter(student=request.user)

    ActvsStudentAttending=Activity.objects.filter(attendee=attendee)
    ActvsStudentVolunteering=Activity.objects.filter(volunteer=volunteer)

    if act.attendee.filter(student=request.user).exists():
        messages.error(request, 'You\'re already registered as an attendee for this activity!', extra_tags='alert')
        return redirect('home/#work')
    elif act.volunteer.filter(student=request.user).exists():
        messages.warning(request, 'You\'re already registered as a volunteer for this activity!', extra_tags='alert')
        return redirect('home/#work')

    elif ActvsStudentVolunteering.exists():
        for x in ActvsStudentVolunteering:
            if x.startDate.date() == act.startDate.date():
                messages.error(request, 'You\'re already registered in the '+x.title+' activity that is held on the same day as '+act.title+'!', extra_tags='alert')
                return redirect('home/#work')

    elif ActvsStudentAttending.exists():
        for x in ActvsStudentAttending:
            if x.startDate.date() == act.startDate.date():
                messages.error(request, 'You\'re already registered in the '+x.title+' activity that is held on the same day as '+act.title+'!', extra_tags='alert')
                return redirect('home/#work')
    else:
        act.volunteer.add(volunteer)
        messages.success(request, 'You\'re successfully registered as a volunteer!', extra_tags='alert')
        return redirect('home/#work')


def cancel(request,pk):
    act = Activity.objects.get(pk=pk)
    act.save()
    attendee, _ = Attendee.objects.get_or_create(student=request.user)
    volunteer, _ = Volunteer.objects.get_or_create(student=request.user)
    act.attendee.remove(attendee)
    act.volunteer.remove(volunteer)
    messages.success(request, 'You successfully Cancelled Your Registration!', extra_tags='alert')
    return redirect('home/#work')
    

# def reset(request):
#     return render(request, 'reset.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!',extra_tags='alert')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.',extra_tags='alert')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })