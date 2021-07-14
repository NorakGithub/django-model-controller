from django.contrib import admin

from model_controller.mixins import ModelControllerAdminMixin


class ModelControllerAdmin(ModelControllerAdminMixin, admin.ModelAdmin):
    pass


class InlineModelControllerAdmin(ModelControllerAdminMixin, admin.InlineModelAdmin):
    pass


class StackedInlineModelControllerAdmin(ModelControllerAdminMixin, admin.StackedInline):
    pass


class TabularInlineModelControllerAdmin(ModelControllerAdminMixin, admin.TabularInline):
    pass
