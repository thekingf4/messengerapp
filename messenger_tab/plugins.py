# -*- coding: utf-8 -*-


from django.conf import settings
from django.utils.translation import ugettext_noop

from lms.djangoapps.courseware.tabs import EnrolledTab
from xmodule.tabs import TabFragmentViewMixin

class MessengerAppTab(TabFragmentViewMixin, EnrolledTab):
    type = 'messenger_tab'
    title = ugettext_noop('Mensajeria')
    priority = None
    view_name = 'messengerapp_view'
    is_hideable = True

    @classmethod
    def is_enabled(cls, course, user=None):
        """
        Returns true if the specified user has staff access.
        """
        return True
       
