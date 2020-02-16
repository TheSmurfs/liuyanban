from django.shortcuts import render


def message_form(request):
    return render(request, "message_form.html")

# Create your views here.
