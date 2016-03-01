from rest_framework.test import APITestCase

class PlaceApiTest(APITestCase):
    def test_get_places_endpoint_should_return_all_places(self):
        response = self.client.get('/places/')

        self.assertEqual(200, response.status_code)
