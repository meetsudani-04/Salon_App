from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.defaultfilters import first

from salon_admin_app.admin_helper import send_email
from salon_user_app.models.customer_models import CustomerModel


@login_required()
def view_customer_views(request):
    template_name = "customer/customer.html"
    customers_obj = CustomerModel.objects.all().values().order_by("-id")
    print(customers_obj)

    # search by name
    search_name = request.GET.get("search_name", "")
    if search_name:
        customers_obj = customers_obj.filter(
            Q(first_name__icontains=search_name) | Q(last_name__icontains=search_name)
        )
    # search by email
    search_email = request.GET.get("search_email", "")
    if search_email:
        customers_obj = customers_obj.filter(email=search_email)

    # Filter by is_active
    is_active = request.GET.get("is_active")
    if is_active in ["1", "0"]:
        customers_obj = customers_obj.filter(is_active=(is_active == "1"))

    context = {
        "search_name":search_name,
        "search_email":search_email,
        "is_active":is_active,
        "customers_obj": customers_obj

    }
    return render(request, template_name,context)

@login_required()
def edit_customer(request , customer_id):
    print("customer_id",customer_id)
    template_name = "customer/edit_customer.html"
    customer = CustomerModel.objects.get(id=customer_id)

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        is_active = request.POST.get("is_active") == "on"

        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email
        customer.password = password
        customer.is_active = is_active
        customer.save()
        return redirect("/salon_admin/customers/")
    context = {
        "customer":customer
    }
    return render(request, template_name,context)

@login_required
def delete_customer(request ,customer_id):
    customer = CustomerModel.objects.get(id=customer_id)
    customer.delete()
    return redirect("/salon_admin/customers/")

