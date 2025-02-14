from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    template_name = "authentication/login.html"
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/salon_admin/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("/salon_admin/login/")
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
