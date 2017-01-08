from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


class ExtendedLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("authentication:login")
