from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from salon_user_app.decorators import session_login_required
from salon_user_app.models.appoiment_book_models import AppointmentBookModel, STATUS_CANCELLED, STATUS_PENDING, \
    STATUS_APPROVED, STATUS_REJECTED


@session_login_required
def view_appointment_history(request):
    template_name = "appointment/appointment_history.html"
    customer_id = request.session.get("customer_id")
    appointment_obj = AppointmentBookModel.objects.filter(customer_id=customer_id).order_by("-id")

    search_status = request.GET.get("search_status", "")
    if search_status:
        appointment_obj = appointment_obj.filter(
            Q(status__icontains=search_status)
        )

    print(search_status)

    context = {
        "appointment_obj": appointment_obj,
        "search_status": search_status,
    }
    return render(request, template_name,context)

@session_login_required
def view_single_appointment(request,appointment_id):
    template_name = "appointment/single_appointment_history.html"
    appointment_obj = AppointmentBookModel.objects.get(id=appointment_id)
    service_list = appointment_obj.services.all()
    context = {
        "appointment_obj": appointment_obj,
        "service_list": service_list,
    }
    return render(request, template_name, context)

@session_login_required
def cancel_appointment(request,appointment_id):
    template_name = "appointment/single_appointment_history.html"
    appointment_obj = AppointmentBookModel.objects.get(id=appointment_id)
    service_list = appointment_obj.services.all()

    if appointment_obj.status == STATUS_PENDING:
        appointment_obj.status = STATUS_CANCELLED
        appointment_obj.save()
        messages.success(request, "Appointment Cancelled Successfully")
    else:
        messages.success(request, "Appointment is already cancelled")
        return redirect("view_appointment_history")
    context = {
        "appointment_obj": appointment_obj,
        "service_list": service_list,
    }
    return render(request, template_name, context)
