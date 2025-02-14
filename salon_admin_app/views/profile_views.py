from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def view_profile(request):
    template_name = "profile.html"
    user_obj = request.user
    print("user",user_obj)

    context = {"user": user_obj,}
    if request.method == "POST":
        username = request.POST.get("username")

        user_obj.username = username
        user_obj.save()
        messages.success(request, "Profile updated successfully")
        return redirect("/salon_admin/view_profile/")

    return render(request, template_name,context)
