from rest_framework.generics import ListAPIView

from places.models import Place
from places.serializers import PlaceSerializer


class PlaceList(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer