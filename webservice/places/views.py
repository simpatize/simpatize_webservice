from rest_framework.generics import ListAPIView

from places.models import Place
from places.serializers import PlaceSerializer


class PlaceList(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):

        places_type_filter = self.request.query_params.get('type')
        queryset = Place.objects.filter(place_type=places_type_filter)
        return queryset