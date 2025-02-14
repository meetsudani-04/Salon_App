from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, redirect

from salon_admin_app.views.authentication.changepass_views import User


@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url="salon_admin")
def view_admin_views(request):
    template_name = "admin/admin.html"
    users = User.objects.all().values()

    # search by name
    search_name = request.GET.get("search_name","")
    if search_name:
        users = users.filter(
            username__icontains=search_name
        )
    # search bt Date of Add Services
    search_doa_start = request.GET.get("search_doa_start", "")
    search_doa_end = request.GET.get("search_doa_end", "")
    date_error_message = ""
    if search_doa_start and search_doa_end:
        if search_doa_end < search_doa_start:
            date_error_message = "End date cannot be earlier than start date."
        else:
            users = users.filter(
                date_joined__gte=search_doa_start, date_joined__lte=search_doa_end
            )
    elif search_doa_start:
        users = users.filter(date_joined__gte=search_doa_start)

    elif search_doa_end:
        users = users.filter(date_joined__lte=search_doa_end)

    # search is_superuser active or inactive
    is_superuser = request.GET.get("is_superuser")
    if is_superuser in ["1", "0"]:
        users = users.filter(is_superuser=(is_superuser == "1"))

    context = {
        "users" : users,
        "search_name":search_name,
        "search_doa_start":search_doa_start,
        "search_doa_end":search_doa_end,
        "date_error_message":date_error_message,
        "is_superuser":is_superuser
        }
    return render(request, template_name,context)

@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url="salon_admin")
def edit_admin(request,admin_id):
    print("admin_id",admin_id)
    template_name = "admin/edit_admin.html"
    users = User.objects.get(id=admin_id)
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        is_superuser = request.POST["is_superuser"]

        users.username = username
        users.email = email
        users.first_name = first_name
        users.last_name = last_name
        users.is_superuser = is_superuser
        users.save()
        return redirect("/salon_admin/admin_views/")
    context = {
        "users" : users
    }
    return render(request, template_name,context)
