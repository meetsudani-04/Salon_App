from django.shortcuts import render


def reset_password(request):
    return render(request, "authentication/resetpass.html")
