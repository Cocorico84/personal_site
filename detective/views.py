from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Place, Suspect, Weapon
from .serializers import PlaceSerializer, SuspectSerializer, WeaponSerializer


class SuspectView(ReadOnlyModelViewSet):
    queryset = Suspect.objects.all()
    serializer_class = SuspectSerializer


class WeaponView(ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class PlaceView(ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
