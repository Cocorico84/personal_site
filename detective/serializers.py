from rest_framework.serializers import ModelSerializer

from .models import Place, Suspect, Weapon


class SuspectSerializer(ModelSerializer):
    class Meta:
        model = Suspect
        fields = "__all__"


class WeaponSerializer(ModelSerializer):
    class Meta:
        model = Weapon
        fields = "__all__"


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
