from rest_framework.generics import ListAPIView

from places.models import Place
from places.serializers import PlaceSerializer


class PlaceList(ListAPIView):
    queryset = Place.objects.all()  #os caras q a gente espere
    serializer_class = PlaceSerializer #o q a gente serializa