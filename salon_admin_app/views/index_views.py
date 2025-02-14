
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from salon_admin_app.models.services import Service
from salon_admin_app.models.services_category_model import ServiceCategory
from salon_user_app.models.appoiment_book_models import AppointmentBookModel

@login_required
def salon_admin(request):
    template_name = "index.html"

    total_appointments_count = AppointmentBookModel.objects.count()
    pending_appointments_count = AppointmentBookModel.objects.filter(status='pending').count()
    total_services_count = Service.objects.count()
    total_services_category_count = ServiceCategory.objects.count()

    context = {
        "total_appointments_count": total_appointments_count,
        "pending_appointments_count": pending_appointments_count,
        "total_services_count": total_services_count,
        "total_services_category_count": total_services_category_count,
    }
    return render(request, template_name,context)
