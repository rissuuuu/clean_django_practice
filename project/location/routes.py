from rest_framework import routers
from location.api.viewsets import ProvinceViewSet,DistrictViewSet

router = routers.DefaultRouter()


router.register("province",ProvinceViewSet)
router.register("district",DistrictViewSet)


urlpatterns = router.urls
