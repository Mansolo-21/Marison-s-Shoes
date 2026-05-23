from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test
)

def is_main_owner(user):

    return (
        user.is_authenticated and
        user.profile.role == 'owner'
    )

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(
            request,
            user,
            backend='django.contrib.auth.backends.ModelBackend'
        )

        return redirect('shop')

    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=login_input,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("shop")

    return render(request, "account/login.html")


def logout_view(request):

    logout(request)

    return redirect(
        'login'
    )


def redirect_user(request):

    if not request.user.is_authenticated:
        return redirect('login')

    role=request.user.profile.role

    if role=="owner":
        return redirect('owner_dashboard')

    elif role=="staff":
        return redirect('owner_dashboard')

    else:
        return redirect('products/shop')

@user_passes_test(is_main_owner)
def promote_user(request, id):

    if request.user.profile.role!="owner":
        return redirect('shop')

    user=User.objects.get(id=id)

    user.profile.role='side_owner'
    user.profile.save()

    return redirect('products/owner_dashboard')