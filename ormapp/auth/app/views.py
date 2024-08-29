from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import customform
from .models import Record

def loginpage(request):
    if request.method == "POST":
        form1 = customform(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data.get("name")
            number = form1.cleaned_data.get("number")
            position=form1.cleaned_data.get('position')

            
            user = authenticate(request, username=name, password=number)

            if user is not None:
                login(request, user)
                messages.success(request, "User successfully logged in")
                return redirect("sign")
            else:
                messages.error(request, "Invalid credentials")
                return redirect("login")  
        else:
        
            messages.error(request, "Form is invalid")
            return render(request, "app/loginpage.html", {"form1": form1})
    else:
        form1 = customform()
        return render(request, "app/loginpage.html", {"form1": form1})


def signpage(request):
    user=request.user

    records = Record.objects.filter(name=user.username)
    
    if records.exists():
        
        record = records.first()  
        
        context = {
            "name": record.name,
            "position": record.position,
            "number":record.number
        }
        return render(request, "app/sign.html", context)
    else:
        
        messages.error(request, "Record does not exist")
        return redirect('login')  
    




