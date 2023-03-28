from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import messengerapp_view

urlpatterns = [
    url(r"^/$", messengerapp_view , name="messengerapp_view")
]

