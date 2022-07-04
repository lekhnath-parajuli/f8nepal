from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from .services import BusinessNameGenerator
from .models import *

NAME_GENERATOR_INPUTS = {
  "name_generator_params": {
    "url": "https://namelix.com/",
    "search": "//*[@id='intro']/form/input[1]",
    "randomness": {
      "go_to": "//*[@id='rootwizard']/ul/li[2]/a",
      "title": "Select generation randomness",
      "choices": {
        "low": "//*[@id='tab_random']/div/div[1]",
        "medium": "//*[@id='tab_random']/div/div[2]",
        "high": "//*[@id='tab_random']/div/div[3]"
      }
    },

    "name_style": {
      "go_to": "//*[@id='rootwizard']/ul/li[3]/a",
      "title": "Select a name style",

      "choices": {
        "auto": "//*[@id='tab_style']/div/div[1]",
        "brandable names": "//*[@id='tab_style']/div/div[2]",
        "alternate spellings": "//*[@id='tab_style']/div/div[3]",
        "non-english words": "//*[@id='tab_style']/div/div[4]",
        "compound words": "//*[@id='tab_style']/div/div[5]",
        "real words": "//*[@id='tab_style']/div/div[6]",
        "two words": "//*[@id='tab_style']/div/div[7]",
        "short phrase": "//*[@id='tab_style']/div/div[8]"
      }
      },

    "generate": "//*[@id='rootwizard']/div/ul/li/a"
  }
}

def branding_view(request):
    context = NAME_GENERATOR_INPUTS
    return render(request, 'branding.html', context)

def get_business_names(request):
    context = {}
    name_generator = NAME_GENERATOR_INPUTS['name_generator_params']
    if request.method == 'POST':
        form = request.POST.dict()
        url = name_generator['url']
        keywords = form.get('key-words')
        selections = {
            "randomness": {
                "go to": name_generator['randomness']['go_to'],
                "choice": form.get('randomness-selection')
                },
                "name style": {
                    "go to": name_generator['name_style']['go_to'],
                    "choice": form.get('name-style-selection'),
                },
                "generate": form.get('business-name-generator')
            }
        BNG = BusinessNameGenerator(url, keywords, selections)
        context = {
            "names": BNG.get_names()
        }

    return render(request, './generator/business-names.html', context)


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