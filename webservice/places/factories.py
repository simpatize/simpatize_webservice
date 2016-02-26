from factory.django import DjangoModelFactory

from places.models import Place


class PlaceFactory(DjangoModelFactory):
    class Meta:
        model = Place