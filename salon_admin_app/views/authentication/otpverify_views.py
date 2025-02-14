from django.shortcuts import render



def otp_verify(request):

    return render(request, "authentication/otpverify.html")
