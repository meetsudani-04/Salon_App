from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import render, redirect

from salon_admin_app.models.services import Service
from salon_user_app.models.appoiment_book_models import AppointmentBookModel, STATUS_PENDING, \
    STATUS_APPROVED, STATUS_REJECTED, STATUS_CANCELLED, STATUS_CHOICES


@login_required
def view_appointment(request):
    template_name = "appointments/view_booked_appointments.html"
    appointment_obj = AppointmentBookModel.objects.all().order_by("-id")

    # search status
    search_status = request.GET.get("search_status", "")
    if search_status:
        appointment_obj = appointment_obj.filter(
            Q(status__icontains=search_status)
        )

    # search by name
    search_name = request.GET.get("search_name", "")
    if search_name:
        appointment_obj = appointment_obj.filter(
            name__icontains = search_name
        )

    # search by email
    search_email = request.GET.get("search_email", "")
    if search_email:
        appointment_obj = appointment_obj.filter(email=search_email)

    # search bt Date of Add Services
    search_doa_start = request.GET.get("search_doa_start", "")
    search_doa_end = request.GET.get("search_doa_end", "")
    date_error_message = ""
    if search_doa_start and search_doa_end:
        if search_doa_end < search_doa_start:
            date_error_message = "End date cannot be earlier than start date."
        else:
            appointment_obj = appointment_obj.filter(
                date__gte=search_doa_start, date__lte=search_doa_end
            )
    elif search_doa_start:
        appointment_obj = appointment_obj.filter(date__gte=search_doa_start)
    elif search_doa_end:
        appointment_obj = appointment_obj.filter(date__lte=search_doa_end)

    context = {
        "appointment_obj": appointment_obj,
        "search_name":search_name,
        "search_email":search_email,
        "date_error_message":date_error_message,
        "search_doa_start":search_doa_start,
        "search_doa_end":search_doa_end,
        "status_choices":STATUS_CHOICES
    }
    return render(request, template_name,context)

@login_required
def edit_appointment(request ,appointment_id):
    user = request.user

    template_name = "appointments/edit_booked_appointment.html"
    appointment_obj = AppointmentBookModel.objects.get(id=appointment_id)
    selected_service_ids = list(appointment_obj.services.values_list("id", flat=True))
    services_list = Service.objects.all().order_by("-id")

    if request.method == "POST":
        if user.is_superuser:
            name = request.POST["name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            service_ids = request.POST.getlist("services")
            appointment_obj.name = name
            appointment_obj.email = email
            appointment_obj.phone = phone
            appointment_obj.services.clear()
            appointment_obj.services.add(*service_ids)
        status = request.POST["status"]
        remark = request.POST["remark"]

        appointment_obj.status = status
        appointment_obj.remark = remark
        appointment_obj.save()
        return redirect("view_appointment")

    print(appointment_obj.status)
    context = {
        "appointment_obj": appointment_obj,
        "services_list": services_list,
        "selected_service_ids": selected_service_ids,
        "status_choices": STATUS_CHOICES,

    }
    return render(request, template_name,context)
