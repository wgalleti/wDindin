from rest_framework import serializers


class BaseModelCreatedSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
