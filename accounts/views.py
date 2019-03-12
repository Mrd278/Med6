#python first
#djang second
#your apps
#local directory
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from .forms import ProfileForm,Booking_form
from .models import patient,hospital,Department,doctor_info,time




# Create your views here.
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log the User
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            login(request,user)
            return redirect('accounts:index')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user in
            user=form.get_user()
            login(request,user)
            return redirect('http://127.0.0.1:8000/accounts/profile/')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def profile(request):
    form=ProfileForm()
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.save()
        else:
            form=ProfileForm()
        return render(request,'accounts/profile_form.html',{'form':form})
    return render(request, 'accounts/profile_form.html', {'form': form})


def booking(request):
    h=hospital.objects.all()
    d=Department.objects.all()
    doc=doctor_info.objects.all()
    timing=time.objects.all()
    form1=Booking_form()
    send_mail('Booking', "Aur launde kaisa h",
              'med6hmaasm@gmail.com',
              ['amaykumar98@gmail.com'], fail_silently=True)
    if request.method=='POST':
        form1= Booking_form(request.POST)
        if form1.is_valid():
            book=form1.save(commit=False)
            book.save()
        else:
            form1=Booking_form()
        return render(request,'accounts/login.html',{'form1':form1,'h':h,'d':d,'doc':doc,'timing':timing})
    return render(request, 'accounts/login.html', {'form1':form1,'h': h, 'd': d, 'doc': doc, 'timing': timing})

