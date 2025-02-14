from django.db.models import Q
from django.shortcuts import render, redirect

from salon_admin_app.models.services import Service
from salon_admin_app.models.services_category_model import ServiceCategory


def user_view_services(request):
    template_name = "services\service1.html"
    services_list = Service.objects.all().order_by("-id")
    print(services_list)

    # search by name
    search_name = request.GET.get("search_name","")
    if search_name:
        services_list = services_list.filter(
            name__icontains=search_name
        )
    # search by category
    category_list = ServiceCategory.objects.all()
    search_category = int(request.GET.get("search_category", 0) or 0)
    if search_category:
        services_list = services_list.filter(
            Q(category_id=search_category)
        )
    # search by price
    search_price_min = request.GET.get("search_price_min", "")
    search_price_max = request.GET.get("search_price_max", "")
    if search_price_min:
        services_list = services_list.filter(price__gte=search_price_min)
    if search_price_max:
        services_list = services_list.filter(price__lte=search_price_max)

    context = {
        "services_list":services_list,
        "search_name":search_name,
        "category_list":category_list,
        "search_category":search_category,
        "search_price_min":search_price_min,
        "search_price_max":search_price_max,
    }
    return render(request, template_name,context)
