from django.conf import settings

from allauth.account.adapter import DefaultAccountAdapter


class AllAuthCustomAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        """
        Whether to allow sign ups.
        """
        if request.resolver_match.view_name == 'account_signup':
            return False
        else:
            return super(AllAuthCustomAdapter, self).is_open_for_signup(request)

    # disable password reset for now
    def send_mail(self, template_prefix, email, context):
        pass
