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
        self.assertEqual(3, len(response.data), 'Should return 3 places.')

    def test_filter_place_by_type_should_return_many_places_of_that_type(self):
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="restaurant")

        response = self.client.get('/places/?type=bar')

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data), 'Should return 2 places.')

    def test_filter_place_by_type_without_matches_should_return_empty_list(self):
        response = self.client.get('/places/?type=bar')

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data), 'When filter does not match anything, no results should be returned.')

    def test_filter_place_by_empty_type_string_should_return_all_results(self):
        PlaceFactory(place_type="bar")
        PlaceFactory(place_type="restaurant")
        response = self.client.get('/places/?type=')

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data), 'When passing an empty string as type filter, all 2 results should be returned ')
