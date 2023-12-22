from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    """ Use instead of serializers.Serializer """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
