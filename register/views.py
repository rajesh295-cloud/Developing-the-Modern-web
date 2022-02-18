from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError


# Create your views here.

def signupform(request):
    return render(request, 'signup.html')


def signupform_save(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['firstname'],
                                            last_name=request.POST['lastname'],
                                            email=request.POST['email'], password=request.POST['password'])
            user.save()
            messages.info(request, "Successfully Created.You can Sign In.")
            return redirect('signin')

        except IntegrityError:
            messages.error(request, "Username Already Exists.Please Try again Another One.")
            return redirect('signup')


def signinform(request):
    return render(request, 'signin.html')


def signinauth(request):
    if request.method == "GET":
        return render(request, 'signin.html')

    else:
        auth_user = authenticate(username=request.POST['authusername'], password=request.POST['authpassword'])
        print(auth_user)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('index')

        else:
            messages.error(request, "Invalid username or password.")
            return redirect('signin')


def signout(request):
    logout(request)
    return redirect('/')


