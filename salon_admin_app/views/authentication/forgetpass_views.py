from django.shortcuts import render


def forget_password(request):
    return render(request, "authentication/forgetpass.html")