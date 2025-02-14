from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from salon_user_app.helper import send_email
from salon_user_app.models.customer_models import CustomerModel


def user_reset_password_view(request):
    template_name = "authentication/user_resetpass.html"
    context = {}

    if "cid" not in request.session:
        return redirect("/forget_password")

    cid = request.session["cid"]
    customer = CustomerModel.objects.filter(id=cid).first()
    if not customer:
        return redirect("/forget_password")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        print(cid)
        print(customer)

        if new_password != confirm_password:
            return render(request, template_name, context)
        if customer:
            customer.password = make_password(new_password)
            customer.save()
            del request.session["cid"]
            send_email(
                subject="Reset Password Request",
                template_name="mail_templates/resetpass_mail.html",
                context={
                    "customer": customer,
                },
                recipient_email=customer.email,
            )
            return redirect("/login")

    return render(request, template_name, context)
