from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    list_serializer_class = None

    def list(self, request, *args, **kwargs):
        if bool(self.request.query_params.get("all", False)):
            self.pagination_class = None

        if self.list_serializer_class is not None:
            self.serializer_class = self.list_serializer_class

        return super().list(request, *args, **kwargs)
