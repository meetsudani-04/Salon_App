import datetime

from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode

from salon_user_app.models.customer_otp_models import CustomerOTP


def user_otp_verify_view(request, cid):
    template_name = "authentication/user_otpverify.html"
    encoded_cid = cid
    cid = urlsafe_base64_decode(encoded_cid).decode("utf-8")

    try:
        customer_otp_obj =CustomerOTP.objects.filter(customer_id=cid).first()
    except ValueError:
        return redirect("/forget_password")

    if not customer_otp_obj:
        return redirect("/forget_password")

    context = {"cid":encoded_cid,}

    if request.method == "POST":
        first = request.POST.get("first")
        second = request.POST.get("second")
        third = request.POST.get("third")
        fourth = request.POST.get("fourth")
        fifth = request.POST.get("fifth")
        sixth = request.POST.get("sixth")
        is_error = False

        if not all ([first,second,third,fourth,fifth,sixth]):
            context["error"] = "All fields are required"
            is_error = True

        if not is_error :
            entered_otp = f"{first}{second}{third}{fourth}{fifth}{sixth}"
            print(entered_otp)
            updated_at = timezone.localtime(customer_otp_obj.updated_at)
            expiration_time = updated_at + datetime.timedelta(minutes=2)
            current_time = timezone.now()

            if current_time > expiration_time:
                context["error"] = "OTP has expired. Please resend OTP."
                return render(request, template_name, context)

            if entered_otp == customer_otp_obj.otp:
                customer_otp_obj.delete()
                request.session["cid"] = cid
                return redirect(f"/reset_password/")
            else:
                context["error"] = "Invalid OTP. Please try again."
                return render(request, template_name, context)

    return render(request, template_name, context)

