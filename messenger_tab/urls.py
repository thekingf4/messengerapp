# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.conf import settings
from .views import MessengerAppView

urlpatterns = (
    url(
        r'courses/{}/messenger$'.format(
            settings.COURSE_ID_PATTERN,
        ),
        MessengerAppView.as_view(),
        name='messengerapp_view',
   ),
 )