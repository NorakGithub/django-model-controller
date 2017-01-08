from django.contrib import admin

from model_controller.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS


class ModelControllerAdmin(admin.ModelAdmin):
    exclude = EXCLUDE_MODEL_CONTROLLER_FIELDS

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_user = request.user
        obj.updated_user = request.user
        obj.save()
