from salon_user_app.models.customer_models import CustomerModel


def customer_info(request):
    customer_id = request.session.get("customer_id")
    customer = CustomerModel.objects.filter(id=customer_id).first()
    print(customer)
    return {'customer': customer}