from braces.views import LoginRequiredMixin
from django.conf import settings

from model_controller.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS


class ExtendedLoginRequiredMixin(LoginRequiredMixin):
    login_url = settings.LOGIN_URL


class ModelControllerAdminMixin(object):
    exclude = EXCLUDE_MODEL_CONTROLLER_FIELDS

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_user = request.user
        obj.updated_user = request.user
        obj.save()
