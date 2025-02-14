from django.core.mail import send_mail
from django.http import HttpResponse


def send_email_view(request):
    send_mail(
        subject="Testing subject",
        message="Hello world",
        from_email=None,
        # from_email=settings.EMAIL_HOST_USER,
        recipient_list=["mayur.python@mailinator.com"],
        # fail_silently=True,
    )
    return HttpResponse("Mail send successfully.")
