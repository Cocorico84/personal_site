from django.urls import include, path
from rest_framework import routers

from .views import PlaceView, SuspectView, WeaponView

router = routers.DefaultRouter()
router.register("suspects", SuspectView)
router.register("weapons", WeaponView)
router.register("places", PlaceView)


urlpatterns = [
    path("", include(router.urls)),
]
