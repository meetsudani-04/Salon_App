from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from salon_user_app.helper import send_email
from salon_user_app.models.customer_models import CustomerModel


def user_signup_view(request):
    template_name = "authentication/user_signup.html"
    context = {}
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        is_error = False
        print(fname, lname, email, password, confirm_password)
        raw_password = make_password(password)

        # back-end validness
        if not all([fname,lname,email,password,confirm_password]):
           context["error"] = "All fields are required"
           is_error = True

        if password != confirm_password:
            context["error"] = "Password and Confirm password do not match"
            is_error = True

        if CustomerModel.objects.filter(email=email).exists():
            context["error"] = "Email already exists"
            is_error = True

        if not is_error:
            customer = CustomerModel(
                first_name = fname,
                last_name = lname,
                email = email,
                password = raw_password,
            )
            customer.save()
            send_email(
                subject="Signup",
                template_name="mail_templates/user_signup_mail.html",
                context={"customer": customer, "message": f"Welcome {fname}"},
                recipient_email=email,
            )
            return redirect("/login/")
    return render(request, template_name, context)