from unittest import TestCase
from views.charts import get_json_url


class TestGet_urls(TestCase):

    def setUp(self):
        self.expected_url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=21%20Jul%202017/' \
                            'EndDate=24%20Jul%202017/Json'

    def test_get_urls(self):
        url = get_json_url('MY1', 3)
        self.assertEqual(url.status_code, 200)
