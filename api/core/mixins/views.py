from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        if bool(self.request.query_params.get("all", False)):
            self.pagination_class = None

        return super().list(request, *args, **kwargs)
