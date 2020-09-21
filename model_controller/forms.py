from django import forms


class BaseModelControllerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'request') or self.request is None:
            self.request = kwargs.pop('request', None)
        super(BaseModelControllerForm, self).__init__(*args, **kwargs)
        try:
            from crispy_forms import FormHelper
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
        except ImportError:
            pass


class ModelControllerForm(BaseModelControllerForm):
    """
    Extend this class when you want to automatically set created_user
    and updated_user to the current login user.

    NOTE: In order for this class to work properly your view you
    must extended BaseCreateView.

    View need to pass request to form kwargs.
    """

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.created_user = self.request.user
        self.instance.updated_user = self.request.user

        return super(ModelControllerForm, self).save(commit=commit)


class ModelControllerWithoutForeignKeyForm(BaseModelControllerForm):
    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.created_user_id = self.request.user.id
        self.instance.updated_user_id = self.request.user.id
        return super(ModelControllerWithoutForeignKeyForm, self).save(commit=commit)
