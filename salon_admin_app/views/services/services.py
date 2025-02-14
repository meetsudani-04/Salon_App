from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from unicodedata import category

from salon_admin_app.models.services import Service
from salon_admin_app.models.services_category_model import ServiceCategory

@login_required
def view_services(request):
    template_name = "services/view_services.html"
    services_list = Service.objects.all().order_by("-id")
    print(services_list)

    # search by name
    search_name = request.GET.get("search_name","")
    if search_name:
        services_list = services_list.filter(
            Q(name__icontains=search_name)
        )

    # search by category
    category_list = ServiceCategory.objects.all()
    search_category = int(request.GET.get("search_category",0)or 0)
    if search_category:
        services_list = services_list.filter(
            Q(category_id=search_category)
        )

    # search bt Date of Add Services
    search_doa_start = request.GET.get("search_doa_start", "")
    search_doa_end = request.GET.get("search_doa_end", "")
    date_error_message = ""
    if search_doa_start and search_doa_end:
        if search_doa_end < search_doa_start:
            date_error_message = "End date cannot be earlier than start date."
        else:
            services_list = services_list.filter(
                created_at__gte=search_doa_start, created_at__lte=search_doa_end
            )
    elif search_doa_start:
        services_list = services_list.filter(created_at__gte=search_doa_start)

    elif search_doa_end:
        services_list = services_list.filter(created_at__lte=search_doa_end)
    print(services_list)

    context = {
        "services_list": services_list,
        "search_name": search_name,
        "category_list": category_list,
        "search_category": search_category,
        "date_error_message": date_error_message,
        "search_doa_start": search_doa_start,
        "search_doa_end": search_doa_end,
    }

    return render(request, template_name, context)

@login_required
def add_services(request):
    template_name = "services/add_services.html"
    services_category_list = ServiceCategory.objects.all().order_by("-id").values()
    print(services_category_list)
    context = {
        "services_category_list": services_category_list
    }
    if request.method == "POST":
        name = request.POST["name"]
        category_id = request.POST["category"]
        price = request.POST["price"]
        duration = request.POST["duration"]
        is_error = False
        print(name,category_id,price,duration)
        if not all([name,category_id,price,duration]):
            context["error"] = "All fields are required"
            is_error = True
        if not is_error:
            services_obj = Service(name=name,category_id=category_id,price=price,duration=duration)
            services_obj.save()
            return redirect("view_services")
    return render(request, template_name,context)

@login_required
def edit_services(request , service_id):
    template_name = "services/add_services.html"
    services_category_list = ServiceCategory.objects.all()

    services_obj = Service.objects.get(id=service_id)
    context = {
        "services_obj": services_obj,
        "services_category_list": services_category_list
    }
    if request.method == "POST":
        name = request.POST["name"]
        category_id = request.POST["category"]
        price = request.POST["price"]
        duration = request.POST["duration"]
        is_error = False
        print(name, category_id, price, duration)
        if not all([name,category_id,price,duration]):
            context["error"] = "All fields are required"
            is_error = True
        if not is_error:
            services_obj.name = name
            services_obj.category_id = category_id
            services_obj.price = price
            services_obj.duration = duration
            services_obj.save()
            return redirect("view_services")
    print("services_obj",services_obj)
    return render(request, template_name, context)

@login_required
def delete_services(request ,s_id):
    services_obj = Service.objects.get(id=s_id)
    services_obj.delete()
    return redirect("view_services")
