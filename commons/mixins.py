from braces.views import LoginRequiredMixin
from django.conf import settings


class ExtendedLoginRequiredMixin(LoginRequiredMixin):
    login_url = settings.LOGIN_URL
