from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from salon_user_app.models.customer_models import CustomerModel

def user_login_view(request):
    template_name = "authentication/user_login.html"
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        is_error = False
        if not all([email, password]):
            context["error_message"] = "Please enter all fields"
            is_error = True

        if not is_error:
            customer_obj = CustomerModel.objects.filter(email=email).first()
            if customer_obj:
                if check_password(password, customer_obj.password):
                    request.session["customer_id"] = customer_obj.id
                    return redirect("/")
                else:
                    context["error_message"] = "Password is incorrect"
            else:
                context["error_message"] = "Email does not exist"

    return render(request, template_name, context)

def user_logout_view(request):
    if "customer_id" in request.session:
        del request.session["customer_id"]
    return redirect('salon_user')