from rest_framework import viewsets

from core.api.serializers import UserSerializerV1
from core.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerV1
