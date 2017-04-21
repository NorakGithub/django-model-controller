try:
    from rest_framework import serializers
except ImportError:
    raise ImportError("Make sure you installed Django Rest Framework before using serializer.")


class ModelControllerSerializer(serializers.ModelSerializer):

    class Meta:
        abstract = True

    def create(self, validated_data):
        user = self.context['request'].user

        validated_data['created_user'] = user
        validated_data['updated_user'] = user

        return super(ModelControllerSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user

        validated_data['updated_user'] = user

        return super(ModelControllerSerializer, self).update(instance, validated_data)
