from django.shortcuts import render

def salon_user(request):
    template_name = "user_index.html"
    context = {}

    return render(request, template_name,context)