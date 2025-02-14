from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from salon_admin_app.models.services_category_model import ServiceCategory

@login_required
def view_services_category(request):
    template_name = "services_category/view_services_category.html"
    services_category_list = ServiceCategory.objects.all().order_by("-id")

    search_name = request.GET.get("search_name","")
    if search_name:
        services_category_list = services_category_list.filter(Q(name__icontains=search_name))

    # search bt Date of Add Services
    search_doa_start = request.GET.get("search_doa_start", "")
    search_doa_end = request.GET.get("search_doa_end", "")
    date_error_message = ""
    if search_doa_start and search_doa_end:
        if search_doa_end < search_doa_start:
            date_error_message = "End date cannot be earlier than start date."
        else:
            services_category_list = services_category_list.filter(
                created_at__gte=search_doa_start, created_at__lte=search_doa_end
            )
    elif search_doa_start:
        services_category_list = services_category_list.filter(created_at__gte=search_doa_start)

    elif search_doa_end:
        services_category_list = services_category_list.filter(created_at__lte=search_doa_end)

    context = {
        "services_category_list":services_category_list,
        "search_name":search_name,
        "date_error_message":date_error_message,
        "search_doa_start":search_doa_start,
        "search_doa_end":search_doa_end,
    }

    return render(request, template_name,context)

@login_required
def add_services_category(request):
    template_name = "services_category/add_services_category.html"
    context = {}
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        is_error = False
        print(name)
        print(description)
        if not all([name,description]):
            context["error"] = "All fields are required"
            is_error = True
        if not is_error:
            services_category_obj = ServiceCategory(
                name = name,
                description = description
            )
            services_category_obj.save()
            return redirect("/view_services_category/")
    return render(request, template_name, context)

@login_required
def edit_services_category(request, sc_id):
    template_name = "services_category/add_services_category.html"
    services_category_obj = ServiceCategory.objects.get(id=sc_id)
    context = {
        "services_category_obj": services_category_obj
    }
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        if not all([name,description]):
            context["error"] = "All fields are required"
            is_error = True
        if not is_error:
            services_category_obj.name =name
            services_category_obj.description =description
            services_category_obj.save()
            return redirect("view_services_category")
    return render(request, template_name, context)

@login_required
def delete_services_category(request, sc_id):
        services_category_obj = ServiceCategory.objects.get(id=sc_id)
        services_category_obj.delete()
        return redirect("view_services")
