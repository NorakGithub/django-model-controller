from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from model_controller.mixins import ExtendedLoginRequiredMixin


class CreateViewMixin(ExtendedLoginRequiredMixin, CreateView):
    """
    This view mixin work together with CreateForm.
    CreateForm need require request to get current login user.
    """
    def get_form_kwargs(self):
        kwargs = super(CreateViewMixin, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class UpdateViewMixin(ExtendedLoginRequiredMixin, UpdateView):

    def get_form_kwargs(self):
        kwargs = super(UpdateViewMixin, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class ListViewMixin(ExtendedLoginRequiredMixin, ListView):
    pass


class DetailViewMixin(ExtendedLoginRequiredMixin, DetailView):
    pass


class DeleteViewMixin(ExtendedLoginRequiredMixin, DeleteView):
    pass
