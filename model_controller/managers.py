from django.db import models

from model_controller.queryset import SoftDeletionQuerySet


class SoftDeletionManager(models.Manager):
    use_for_related_fields = True

    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        qs = super(SoftDeletionManager, self).get_queryset()

        if self.alive_only:
            qs = qs.filter(alive=True)

        if not issubclass(qs.__class__, SoftDeletionQuerySet):
            qs.__class__ = SoftDeletionQuerySet
        return qs

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def cascade_delete(self):
        return self.get_queryset().cascade_delete()

    def restore(self):
        return self.get_queryset().restore()

    def cascade_restore(self):
        return self.get_queryset().cascade_restore()
