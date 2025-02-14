from django.contrib import admin

from .models.services import Service
from .models.services_category_model import ServiceCategory

admin.site.register(ServiceCategory)
admin.site.register(Service)