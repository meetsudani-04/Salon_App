from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

from salon_user_app.decorators import session_login_required
from salon_user_app.models.customer_models import CustomerModel
from salon_user_app.views.authentication.user_login_views import user_logout_view


@session_login_required
def user_profile_views(request):
    template_name = "profile/user_profile.html"
    customer_id = request.session.get("customer_id")
    customer = CustomerModel.objects.filter(id=customer_id).first()
    context = {
        "customer": customer,
    }
    return render(request, template_name, context)

@session_login_required
def edit_user_profile_views(request):
    template_name = "profile/user_profile.html"
    customer_id = request.session.get("customer_id")
    customer = CustomerModel.objects.filter(id=customer_id).first()
    context = {"customer": customer}

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        profile_pic = request.FILES.get("profile_pic")
        is_error = False

        if not all([first_name,last_name,phone]):
            context["error"] = "All fields are required"
            is_error = True

        if not is_error:
            customer.first_name = first_name
            customer.last_name = last_name
            customer.phone = phone
            if profile_pic:
                customer.profile_pic = profile_pic
            customer.save()

            return redirect("/profile/")
    return render(request, template_name, context)

@session_login_required
def user_change_password_view(request):
    template_name = "profile/user_change_password.html"
    customer_id = request.session.get("customer_id")
    customer = CustomerModel.objects.filter(id=customer_id).first()
    print(customer.password)
    context = {"customer": customer}

    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        is_error = False

        if not all([current_password ,new_password, confirm_password]):
            context["error"] = "All fields are required"
            is_error = True

        elif new_password != confirm_password:
            context["error"] = "New password and Confirm password do not match"
            is_error = True

        elif not check_password(current_password,customer.password):
            context["error"] = "Current password is incorrect"
            is_error = True

        if not is_error:
            customer.password = make_password(new_password)
            customer.save()

            user_logout_view(request)
            context["success"] = "Password changed successfully. Please log in again."
            # context["error"] = "Password changed successfully"
            return redirect("/profile/")

    return render(request, template_name, context)
