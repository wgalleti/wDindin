from rest_framework import routers
from .api.views import (
    BankViewSetV1,
    BankAccountViewSetV1,
    CategoryViewSetV1,
    TransactionViewSetV1,
    CreditCardViewSetV1,
)

router = routers.DefaultRouter()

router.register("banks", BankViewSetV1)
router.register("accounts", BankAccountViewSetV1)
router.register("cards", CreditCardViewSetV1)
router.register("categories", CategoryViewSetV1)
router.register("transactions", TransactionViewSetV1)

urlpatterns = router.urls
