import os
import time
from uuid import uuid4

from django.utils.deconstruct import deconstructible

EXCLUDE_MODEL_CONTROLLER_FIELDS = ('created_at', 'updated_at', 'created_user', 'updated_user')


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        # allow to customize path in __call__
        self.path = path

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return os.path.join(self.path, "%s-%s%s") % (
            time.strftime("%Y%m%d-%H%M%S"),
            uuid4(),
            extension
        )
