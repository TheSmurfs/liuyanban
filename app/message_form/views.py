from django.shortcuts import render
from app.message_form.models import Message


def message_form(request):
    return render(request, "message_form.html")


# Create your views here.


def message_from(request):
    all_messages = Message.objects
    for message in all_messages:
        print(message.name)
    return render(request, "message_form.html")
