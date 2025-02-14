import datetime
import random
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from salon_user_app.models.customer_otp_models import CustomerOTP

# send mail
def send_email(subject, template_name, context, recipient_email, from_email=None):
    email_body = render_to_string(template_name, context)
    send_mail(
        subject=subject,
        message=context.get("message", ""),
        from_email=from_email,
        recipient_list=[recipient_email],
        html_message=email_body,
    )

# send otp mail
def otp_send_email(customer_otp: CustomerOTP):
    send_email(
        subject="Password Reset OTP",
        template_name="mail_templates/otp_mail.html",
        context={"customer": customer_otp.customer, "otp": customer_otp.otp},
        recipient_email=customer_otp.customer.email,
    )

# generate random otp
def generate_random_otp():
    return random.randint(100000, 999999)


# generate_or_get_otp otp
def generate_or_get_otp(customer):
    customer_otp = CustomerOTP.objects.filter(customer=customer).first()
    current_time = timezone.now()

    if customer_otp:
        updated_at = timezone.localtime(customer_otp.updated_at)
        expired_time = updated_at + datetime.timedelta(minutes=2)

        if current_time > expired_time:
            otp = generate_random_otp()
            customer_otp.otp = otp
            customer_otp.updated_at = current_time
            customer_otp.save()
    else:
        otp = generate_random_otp()
        customer_otp = CustomerOTP.objects.create(customer=customer, otp=otp)

    return customer_otp

# resend otp mail
def resend_otp_email(customer):
    customer_otp = generate_or_get_otp(customer)
    otp_send_email(customer_otp)
    return customer_otp
