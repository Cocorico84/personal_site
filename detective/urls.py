from re import template

from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from .views import PlaceView, SuspectView, WeaponView

router = routers.DefaultRouter()
router.register("suspects", SuspectView)
router.register("weapons", WeaponView)
router.register("places", PlaceView)


urlpatterns = [
    path("play", include(router.urls)),
    path("", TemplateView.as_view(template_name="game_index.html"), name="game"),
]
