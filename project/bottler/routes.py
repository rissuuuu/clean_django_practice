from rest_framework import routers
from bottler.api.viewsets import (
    BottlerViewSet,
    DealerBrandViewSet,
    BrandViewSet,
    UserBrandViewSet,
)


router = routers.DefaultRouter()
router.register("bottler", BottlerViewSet)
router.register("dealer_brand", DealerBrandViewSet)
router.register("brand", BrandViewSet)
router.register("user_brand", UserBrandViewSet)


urlpatterns = router.urls
