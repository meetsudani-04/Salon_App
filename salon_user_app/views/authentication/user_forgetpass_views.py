from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode

from salon_user_app.helper import generate_or_get_otp, otp_send_email
from salon_user_app.models.customer_models import CustomerModel


def user_forget_password_view(request):
    template_name = "authentication/user_forgetpass.html"
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        is_error = False
        if not all ([email]):
            context["error"] = "All fields are required"
            is_error = True

        if not is_error:
            customer = CustomerModel.objects.filter(email=email).first()
            if customer:
                # Helper function use generate_or_get_otp
                customer_otp = generate_or_get_otp(customer)
                print("-------------customer_otp",customer_otp.otp)
                otp_send_email(customer_otp)
                user_id_base_64 = urlsafe_base64_encode(str(customer.id).encode('utf-8'))
                return redirect(f"/otp_verify/{user_id_base_64}/")
            else:
                return render(request, template_name, context)
    return render(request, template_name, context)
