from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from .models import Record

from .forms import Addrecords

def mainview(request):
    records=Record.objects.all()
    return render(request, "api/main.html", {"records":records})  

def register_user(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, "user successfully registered")
            return redirect( "main" )

    else:
        form=UserCreationForm()
        return render(request,"api/register.html", {"form":form})
    return render(request,"api/register.html", {"form":form})


def login_user(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in successfully")
            return redirect("main")
        else:
            messages.success(request,"some issues with your credentials")
            return redirect("login")
    else:
        return render( request, "api/login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect( "register" )

from django.shortcuts import get_object_or_404
def customer_record(request,pk):
    if request.user.is_authenticated:
        #cr=Record.objects.get( id=pk) if in Record Model
        cr= Record.objects.get( id=pk)
        return render(request, "api/record.html", { "cr":cr})
    else:
        messages.success(request, "You must login before" )
        return redirect( "login")


def delete_record(request,pk):
    rec=Record.objects.get(id=pk)
    if request.user.is_authenticated:
        rec.delete()
        return redirect("main")
    else:
        messages.success(request, "Need to be logged in")


def add_record(request):
    form = Addrecords(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST" and form.is_valid():
            add_record=form.save()
            messages.success(request, "Record successfully added")
            return redirect("main")
        return render(request, "api/addrecord.html", {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("login")

def modify_record(request, pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=Addrecords( request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated your records")
            return redirect( "main" )
        return render(request, "api/modifyrecord.html", {"form":form})
    else:
        messages.success(request, "you need to be logged in")
        return redirect( "login" )