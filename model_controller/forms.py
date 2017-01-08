from crispy_forms.helper import FormHelper

from django import forms


class ModelControllerForm(forms.ModelForm):
    """
    Extend this class when you want to automatically set created_user
    and updated_user to the current login user.

    NOTE: In order for this class to work properly your view you
    must extended BaseCreateView.

    View need to pass request to form kwargs.
    """

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'request') or self.request is None:
            self.request = kwargs.pop('request', None)
        super(ModelControllerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.created_user = self.request.user
        self.instance.updated_user = self.request.user

        return super(ModelControllerForm, self).save(commit=commit)
