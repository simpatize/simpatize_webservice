from django.test import TestCase
from simpatize_webservice.webservice.google_maps_api import URL


class URL_Tests(TestCase):

    url_from_google = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}"

    def test_should_be_true_anyway(self):
        self.assertEqual(1,1)

    def test_if_request_is_null_URLForJson_should_be_empty(self):
        url_created = URL().create(None)
        self.assertEqual(url_created, "")

    def test_if_request_is_empty_should_return_standard_URLForJson(self):
        url_created = URL().create("")
        self.assertEqual(url_created, self.url_from_google)