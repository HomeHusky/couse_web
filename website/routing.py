from django.urls import re_path, path, url

from . import consumers

websocket_urlpatterns = [
    path("ws/", consumers.WSConsumer.as_asgi()),
]