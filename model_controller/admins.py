from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from model_controller.mixins import ModelControllerAdminMixin


class ModelControllerAdmin(ModelControllerAdminMixin, admin.ModelAdmin):
    pass


class InlineModelControllerAdmin(ModelControllerAdminMixin, InlineModelAdmin):
    pass


class StackedInlineModelControllerAdmin(ModelControllerAdminMixin, admin.StackedInline):
    pass


class TabularInlineModelControllerAdmin(ModelControllerAdminMixin, admin.TabularInline):
    pass
