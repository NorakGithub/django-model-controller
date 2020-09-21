import django
if django.VERSION[0] >= 3 and django.VERSION[1] >= 1:
    from django.db.models import BooleanField as BooleanField
else:
    from django.db.models import NullBooleanField as BooleanField


class LiveField(BooleanField):
    """
    Support uniqueness constraints and soft-deletion.
    Similar to a BooleanField, but stores False as NULL. This lets us use
    database constraints to enforce uniqueness of live objects but still allow
    many duplicate dead objects (treating each NULL as a unique snowflake
    follows the ANSI SQL standard, and works in both MySQL and Postgres).
    """

    def __init__(self, *args, **kwargs):
        super(LiveField, self).__init__(default=True, null=True, db_index=True)

    def get_prep_value(self, value):
        # Convert in-Python value to value we'll store in DB
        if value:
            return super(LiveField, self).get_prep_value(True)
        return None

    def from_db_value(self, value, expression, connection, *args):
        # context param is deprecated in Django 2.x will be removed in Django 3.x
        # having *args allows this code to run in Django 1.x and Django 2.x
        return self.to_python(value)

    def to_python(self, value):
        # Somewhat misleading name, since this type coercion also occurs when
        # assigning a value to the field in Python.
        return bool(value)

    def get_prep_lookup(self, lookup_type, value):
        if lookup_type == 'exact' and not value:
            msg = "%(model)s doesn't support filters or excludes with " \
                  "%(field)s=False. Try using %(field)s=None."
            raise TypeError(
                msg % {'model': self.model.__name__, 'field': self.name})
        return super(LiveField, self).get_prep_lookup(lookup_type, value)
