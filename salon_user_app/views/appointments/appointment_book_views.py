from datetime import datetime

from django.shortcuts import render, redirect

from salon_admin_app.models.services import Service
from salon_user_app.helper import send_email
from salon_user_app.models.appoiment_book_models import AppointmentBookModel

from salon_user_app.decorators import session_login_required
from salon_user_app.models.customer_models import CustomerModel


@session_login_required
def book_appointment(request):
    template_name = "appointment/bookappoiment.html"
    services_list = Service.objects.all().order_by("-id")

    customer_id = request.session.get("customer_id")
    customer = CustomerModel.objects.filter(id=customer_id).first()

    context = {
        "services_list": services_list,
        "customer": customer,
    }

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        service_ids = request.POST.getlist("services")
        date = request.POST["date"]
        appointment_date = datetime.strptime(date, "%d-%m-%y %H:%M")
        is_error = False

        if not all([name,email,phone,service_ids,appointment_date]):
            context["error"] = "All fields are required"
            is_error = True

        if not is_error:
            if not customer.is_active:
                context["error_message"] = "Your account is inactive"
            else:
                appointment_book_obj = AppointmentBookModel(name=name,email=email,phone=phone,date=appointment_date,customer=customer)
                appointment_book_obj.save()
                appointment_book_obj.services.add(*service_ids)
                send_email(
                    subject="Appointment Confirmation",
                    template_name="mail_templates/user_appointment_book_mail.html",
                    context={"appointment_book_obj": appointment_book_obj, "message": f"Welcome {name}"},
                    recipient_email=email,
                )
                return redirect("salon_user")
    return render(request, template_name,context)
