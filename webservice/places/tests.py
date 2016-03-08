from rest_framework.test import APITestCase
import django
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from places.factories import PlaceFactory
django.setup()

class PlaceApiTest(APITestCase):
    def test_get_places_endpoint_should_return_all_places(self):
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="restaurant")
        response = self.client.get('/places/')

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(3, len(response.data), 'test')

    def test_filter_place_by_type_should_return_many_places_of_that_type(self):
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="restaurant")

        response = self.client.get('/places/?type=bar')

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))
