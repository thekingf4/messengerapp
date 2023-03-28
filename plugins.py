from django.utils.translation import ugettext_noop
from lms.djangoapps.courseware.tabs import EnrolledTab

class MessengerTab(EnrolledTab):
    """
    The representation of the course teams view type.
    """
    type = "messengerapp"
    title = ugettext_noop("Mensajeria")
    view_name = "messengerapp"
    is_default = True
    tab_id = "messengerapp"
    is_hideable = True
    view_name = "messengerapp_view"

    @classmethod
    def is_enabled(cls, course, user=None):

        if not super(MessengerTab, cls).is_enabled(course, user=user):
            return False

        if user and not user.is_authenticated:
            return False

        return True

