from django.conf import settings
from django.db import models
from django.db.models import signals
try:
    import django
    major, feature, minor, a, b = django.VERSION
    if major >= 2:
        from django.utils.translation import gettext as _
    else:
        from django.utils.translation import ugettext as _
except ImportError:
    raise SerializerConfigError('Django is required. Please make sure you '
                                'have install via pip.')


from model_controller.fields import LiveField
from model_controller.managers import SoftDeletionManager


class AbstractTimeStampMarker(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at")
    )

    class Meta:
        abstract = True


class AbstractModelController(AbstractTimeStampMarker):
    created_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="%(class)s_created_user",
        verbose_name=_("Created User"),
        on_delete=models.CASCADE
    )
    updated_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="%(class)s_updated_user",
        verbose_name=_("Updated User"),
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class AbstractCreatedUpdatedUsername(models.Model):
    created_username = models.CharField(
        _('Created Username'),
        max_length=200,
        null=True,
        blank=True,
    )
    updated_username = models.CharField(
        _('Updated Username'),
        max_length=200,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class AbstractModelControllerWithoutForeignKey(AbstractTimeStampMarker):
    created_user_id = models.IntegerField(_('Created User ID'))
    updated_user_id = models.IntegerField(
        _('Updated User ID'),
        null=True
    )

    class Meta:
        abstract = True


class AbstractSoftDelete(models.Model):
    """
    Soft delete is used when you don't want to actually delete data from your
    database but just masked that this data has been removed and you restore it
    back by just change alive to True.
    """
    alive = LiveField()

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.alive = None
        self.save()
        signals.post_delete.send(sender=self.__class__, instance=self, using=using)

    def hard_delete(self, using=None, keep_parents=False):
        super(AbstractSoftDelete, self).delete(using, keep_parents)

    def restore(self):
        self.alive = True
        self.save()


class AbstractSoftDeletionModelController(AbstractSoftDelete,
                                          AbstractModelController):

    class Meta:
        abstract = True


class AbstractSoftDeletionModelControllerWithoutForeignKey(
    AbstractSoftDelete,
    AbstractModelControllerWithoutForeignKey
):
    class Meta:
        abstract = True


class AbstractSoftDeletionCreatedUpdatedUsernameTimestamp(
    AbstractSoftDelete,
    AbstractTimeStampMarker,
    AbstractCreatedUpdatedUsername,
):
    class Meta:
        abstract = True
