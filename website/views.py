from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

from rest_framework import viewsets



# from .camera import FacialLandMarksPosition, predict_eye_state

# Create your views here.

count = False


def index(request):
    return render(request, "website/index.html")

def course(request):
    return render(request, "website/course.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def detail(request):
    return render(request, "website/detail.html")

def run(request):
    return render(request, "website/detail.html")

def feature(request):
    return render(request, "website/feature.html")

def team(request):
    return render(request, "website/team.html")

def testimonial(request):
    return render(request, "website/testimonial.html")

def chat(request):
    return render(request,"website/chat.html")

def room(request):
    return render(request, "website/room.html")

def test(request):
    return render(request, "website/test.html", context={'text':'Hello World'})

