from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode

from salon_user_app.helper import resend_otp_email
from salon_user_app.models.customer_models import CustomerModel


def user_resend_otp_view(request,cid):
    encoded_cid = cid
    cid = urlsafe_base64_decode(encoded_cid)
    print(cid)
    if not cid or not cid.isdigit():
        print(cid)
        return redirect("/forget_password")

    customer = CustomerModel.objects.filter(id=cid).first()
    if not customer:
        return redirect("/forget_password")

    # Resend OTP using the helper function
    resend_otp_email(customer)

    return redirect(f"/otp_verify/{encoded_cid}/")
