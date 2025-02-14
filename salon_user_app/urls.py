from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from salon_user_app.views.appointments.appointment_book_views import book_appointment
from salon_user_app.views.appointments.appointment_history_views import view_appointment_history, \
    view_single_appointment, cancel_appointment
from salon_user_app.views.authentication.user_forgetpass_views import user_forget_password_view
from salon_user_app.views.authentication.user_login_views import user_login_view, user_logout_view
from salon_user_app.views.authentication.user_otp_verify_views import user_otp_verify_view
from salon_user_app.views.authentication.user_resend_otp_views import user_resend_otp_view
from salon_user_app.views.authentication.user_resetpass_views import user_reset_password_view
from salon_user_app.views.authentication.user_signup_views import user_signup_view
from salon_user_app.views.profile.user_profile_views import user_profile_views, edit_user_profile_views, \
    user_change_password_view
from salon_user_app.views.services.view_services_views import user_view_services
from salon_user_app.views.user_index_views import salon_user

urlpatterns = [

    path("",salon_user,name="salon_user"),
    # authentication
    path("signup/",user_signup_view,name="user_signup_view"),
    path("login/",user_login_view,name="user_login_view"),
    path("logout/",user_logout_view,name="user_logout_view"),
    path("forget_password/",user_forget_password_view,name="user_forget_password"),
    path("otp_verify/<str:cid>/",user_otp_verify_view,name="user_otp_verify"),
    path("resend_otp/<str:cid>/",user_resend_otp_view,name="user_resend_otp_view"),
    path("reset_password/",user_reset_password_view,name="user_reset_password"),

    path("change_password/",user_change_password_view,name="user_change_password_view"),
    # -----------------------------------------------------------------------------------
    path("profile/",user_profile_views,name="user_profile_views"),
    path("profile/edit",edit_user_profile_views,name="edit_user_profile_views"),
    # -----------------------------------------------------------------------------------
    path("services/",user_view_services,name="services"),
    path("book_appointment/",book_appointment,name="book_appointment"),
    path("appointment/history/",view_appointment_history,name="appointment_history"),
    path("appointment/history/<int:appointment_id>/single",view_single_appointment,name="single_appointment"),
    path('cancel-appointment/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)