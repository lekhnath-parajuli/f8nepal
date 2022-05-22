from email import message
from http import client
from sqlite3 import Date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import EmailMessage
import datetime

from .models import *
from . import forms

def index_view(request, *args, **kwargs):

    context = {
        'clients': Customers.objects.all(),
        'portfolio': Portfolio.objects.all(),
        'team': Team.objects.all(),
        'services': Services.objects.all(),
        'user': request.user,

    }
    return render(request, 'index.html', context)

def feedback_view(request, *args, **kwargs):
    context = {
        "comments" : Feedback.objects.all(),
        'user': request.user,
    }

    return render(request, 'feedback.html', context)

def post_feedback(request, *args, **kwargs):
    context = {
        'user': request.user,

    }

    if request.method == 'POST':
        form = request.POST.dict()
        Catagory = form.get('catagory')
        Rating = form.get('rating')
        FullName = form.get('name')
        Email = form.get('email')
        Comment = form.get('feedback')

        post = Feedback.objects.create(
            Catagory = Catagory,
              Rating = Rating,
            FullName = FullName,
               Email = Email,
             Comment = Comment)
        post.save()

        return render(request, 'index.html', context)
    return render(request, 'index.html', context)


def send_mail(request):
    if request.method == 'POST':
        form = request.POST.dict()
        client_email = form.get('email')
        client_subject = form.get('subject')
        client_message = form.get('message')

        client_message = "sender: "+client_email+"\n"+" "+client_message

        EmailMessage (
            client_subject,# subject of the mail 
            client_message, # message of the sender 
            client_email, # email of the sender
            ["f8nepal@gmail.com"], # To email
        ).send()

    context = {
        'clients': Customers.objects.all(),
        'portfolio': Portfolio.objects.all(),
        'team': Team.objects.all(),
        'services': Services.objects.all(),
        'user': request.user,

    }

    return render(request, 'index.html', context)