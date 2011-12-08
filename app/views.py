import logging

from ecl_django.decorators import render

logger = logging.getLogger(__name__)

@render
def home(request):
    return {}

# XXX Uncomment for Facebook integration
# from ecl_facebook.decorators import facebook_callback
# @facebook_callback
# def oauth_facebook_complete(request, token):
#     facebook = Facebook(token)
#     user = authenticate(id=user.id)
#     login(request, user)
#     return HttpResponseRedirect(user.get_absolute_url())

