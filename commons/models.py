from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractTimeStampMarker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class AbstractModelController(AbstractTimeStampMarker):
    created_user = models.ForeignKey(User, related_name="%(class)s_created_user", verbose_name=_("Created User"))
    updated_user = models.ForeignKey(User, related_name="%(class)s_updated_user", verbose_name=_("Updated User"))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request:
            if not self.pk:
                self.created_by = request.user
            self.updated_by = request.user
        return super(AbstractModelController, self).save(*args, **kwargs)
