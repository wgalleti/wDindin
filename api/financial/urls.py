from rest_framework import routers
from .api.views import (
    BankViewSet,
    BankAccountViewSet,
    CategoryViewSet,
    TransactionViewSet,
)

router = routers.DefaultRouter()

router.register("banks", BankViewSet)
router.register("accounts", BankAccountViewSet)
router.register("categories", CategoryViewSet)
router.register("transactions", TransactionViewSet)

urlpatterns = router.urls
