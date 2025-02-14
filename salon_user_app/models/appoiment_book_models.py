from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.utils.safestring import mark_safe

from salon_admin_app.models.services import Service


STATUS_PENDING = 'pending'
STATUS_APPROVED = 'approved'
STATUS_REJECTED = 'rejected'
STATUS_CANCELLED = 'cancelled'

STATUS_CHOICES = [
    (STATUS_PENDING, 'Pending'),
    (STATUS_APPROVED, 'Approved'),
    (STATUS_REJECTED, 'Rejected'),
    (STATUS_CANCELLED, 'Cancelled'),
]

class AppointmentBookModel(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    services = models.ManyToManyField(Service, related_name='appointments')
    date = models.DateTimeField(help_text="The date and time of the appointment.")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    remark = models.TextField(blank=True, null=True, help_text="Additional comments or notes for the appointment.")
    customer = models.ForeignKey('CustomerModel', on_delete=models.CASCADE, related_name='appointments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.date} - {self.status} {self.services.all().values_list('name', flat=True)} - {self.customer.id}"

    @property
    def total_service_price(self):
        return self.services.aggregate(total_price=Sum('price'))['total_price'] or Decimal('0.00')

    @property
    def total_duration(self):
        return self.services.aggregate(total_duration=Sum('duration'))['total_duration'] or 0

    @property
    def formatted_status(self):
        for status in STATUS_CHOICES:
            if self.status == status[0]:
                return mark_safe(f"<span class='badge badge-{ 'warning' if self.status == STATUS_PENDING else 'success' if self.status == STATUS_APPROVED  else 'info' if self.status == STATUS_REJECTED else 'danger' }'>{status[1]}</span>")
        return self.status


