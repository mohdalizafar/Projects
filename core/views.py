from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    return render(request,"core/home.html")


def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"User {username} logged in successfully")  # Debugging line
                return redirect('home')  # Redirect to the home page after successful login
            else:
                print(f"Authentication failed for {username}")  # Debugging line
                return render(request, 'core/loginpage.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            print(f"Form errors: {form.errors}")  # Debugging line
            return render(request, 'core/loginpage.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'core/loginpage.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect( "home")
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, "core/register.html", context)
