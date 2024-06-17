from rest_framework import serializers

from core.models import User


class UserSerializerV1(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = super().create(validated_data)

        if password:
            instance.set_password(password)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        change_password = password and password != instance.password

        instance = super().update(instance, validated_data)
        if change_password:
            instance.set_password(password)
            instance.save()

        return instance


class TokenUserSerializerV1(UserSerializerV1):
    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "username",
        )


class JWTSerializerV1(serializers.Serializer):
    token = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_token(self, obj):
        return str(obj.get("access"))

    def get_user(self, obj):
        user_data = TokenUserSerializerV1(obj["user"], context=self.context).data
        return user_data
