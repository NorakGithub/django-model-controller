from django.views.generic.edit import ModelFormMixin

from model_controller.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS
from tests.models import Company


class CompanyForm(ModelFormMixin):

    class Meta:
        model = Company
        fields = EXCLUDE_MODEL_CONTROLLER_FIELDS
