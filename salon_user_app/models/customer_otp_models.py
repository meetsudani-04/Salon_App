from django.db import models

from salon_user_app.models.customer_models import CustomerModel


class CustomerOTP(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.otp} - {self.created_at} - {self.updated_at}"