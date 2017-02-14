from __future__ import unicode_literals

from django.db import models

from model_controller.models import AbstractModelController


class Company(AbstractModelController):
    name = models.CharField(max_length=100, verbose_name="Name")
