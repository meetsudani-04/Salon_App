from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

User = get_user_model()

@login_required
def change_password(request):
    user = request.user
    template_name = "authentication/changepass.html"
    context = {}
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = authenticate(username=user.username, password=current_password)

        if user is not None:
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()

                messages.success(request, "Your password was successfully updated!")
                return redirect("/salon_admin/")
            else:
                messages.error(
                    request, "New passwords and Confirm password do not match."
                )
        else:
            messages.error(request, "Old password is incorrect.")

    return render(request, template_name, context)
