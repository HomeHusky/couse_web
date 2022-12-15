from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    # path("<int:month>", views.monthly_challenge_by_number),
    # path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("", views.index, name="index"),
    path("course/", views.course, name="course"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("detail/", views.detail, name="detail"),
    path("feature/", views.feature, name="feature"),
    path("team/", views.team, name="team"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("camera/", views.run, name="camera"),
    path("test/", views.test, name="test"),
    path("chat/", views.chat, name="chat"),
    path("room/", views.room, name="room"),
]
