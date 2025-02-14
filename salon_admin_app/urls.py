from django.urls import path

from .views.admins.admin_views import edit_admin, view_admin_views
from .views.authentication.changepass_views import change_password
from .views.authentication.forgetpass_views import forget_password
from .views.authentication.login_views import login_view, logout_view
from .views.authentication.otpverify_views import otp_verify
from .views.authentication.resetpass_views import reset_password
from .views.customer.customer_views import view_customer_views, edit_customer, delete_customer
from .views.index_views import salon_admin
from .views.profile_views import view_profile
from salon_admin_app.views.appointments.admin_appointment_views import view_appointment, edit_appointment
from .views.services.services import view_services, edit_services, add_services, delete_services
from .views.services_category.services_category_views import add_services_category, view_services_category, \
    edit_services_category, delete_services_category

urlpatterns = [
    path('', salon_admin, name='salon_admin'),
    # authentication
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
    path('forget_password/', forget_password, name='forget_password'),
    path('otp_verify/', otp_verify, name='otp_verify'),
    path('reset_password/', reset_password, name='reset_password'),
    # view_profile
    path('view_profile/', view_profile, name='view_profile'),
    path('change_password/', change_password, name='change_password'),
    # services category
    path('services_category/', view_services_category, name='view_services_category'),
    path('services_category/add/', add_services_category, name='add_services_category'),
    path('services_category/<int:sc_id>/edit/', edit_services_category, name='edit_services_category'),
    path('services_category/<int:sc_id>/delete/', delete_services_category, name='delete_services_category'),
    # services
    path('services/', view_services, name='view_services'),
    path('services/add/', add_services, name='add_services'),
    path('services/<int:service_id>/edit/', edit_services, name='edit_services'),
    path('services/<int:s_id>/delete/', delete_services, name='delete_services'),
    # Appointment
    path('appointment/', view_appointment, name='view_appointment'),
    path('appointment/<int:appointment_id>/edit', edit_appointment, name='edit_appointment'),
    # Admin
    path('admin_views/', view_admin_views, name='admin_views'),
    path('admin_views/<int:admin_id>/edit', edit_admin, name='edit_admin'),
    #Customer
    path('customers/', view_customer_views, name='customer_views'),
    path('customers/<int:customer_id>/edit', edit_customer, name='edit_customer'),
    path('customers/<int:customer_id>/delete', delete_customer, name='delete_customer'),

]

