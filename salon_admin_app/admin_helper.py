from django.core.mail import send_mail
from django.template.loader import render_to_string


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


# # send otp mail
# def otp_send_email(user_otp: UserOTP):
#     send_email(
#         subject="Password Reset OTP",
#         template_name="mail_templates/otp_mail.html",
#         context={"user": user_otp.user, "otp": user_otp.otp},
#         recipient_email=user_otp.user.email,
#     )
#
#
# # generate random otp
# def generate_random_otp():
#     return random.randint(100000, 999999)
#
#
# # generate otp
# def generate_or_get_otp(user):
#     user_otp = UserOTP.objects.filter(user=user).first()
#     current_time = timezone.now()
#
#     if user_otp:
#         updated_at = timezone.localtime(user_otp.updated_at)
#         expired_time = updated_at + datetime.timedelta(minutes=2)
#
#         if current_time > expired_time:
#             otp = generate_random_otp()
#             user_otp.otp = otp
#             user_otp.updated_at = current_time
#             user_otp.save()
#     else:
#         otp = generate_random_otp()
#         user_otp = UserOTP.objects.create(user=user, otp=otp)
#
#     return user_otp
#
#
# # resend otp mail
# def resend_otp_email(user):
#     user_otp = generate_or_get_otp(user)
#     otp_send_email(user_otp)
#     return user_otp
