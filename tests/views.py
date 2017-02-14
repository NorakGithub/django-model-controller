from model_controller.views import CreateViewMixin, ListViewMixin
from tests.forms import CompanyForm


class CompanyListView(ListViewMixin):
    pass


class CompanyCreateView(CreateViewMixin):
    template_name = "tests/create.html"
    form_class = CompanyForm
