from django.contrib import admin

from salon_user_app.models.appoiment_book_models import AppointmentBookModel
from salon_user_app.models.customer_models import CustomerModel
from salon_user_app.models.customer_otp_models import CustomerOTP

admin.site.register(AppointmentBookModel)
admin.site.register(CustomerModel)
admin.site.register(CustomerOTP)
