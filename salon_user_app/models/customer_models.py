
from django.db import models


class CustomerModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    profile_pic = models.ImageField(upload_to="user_profile/",default="user_profile/default.png",)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.email} -  {self.phone} - {self.password} - {self.profile_pic} - {self.is_active} - {self.created_at} - {self.updated_at}"