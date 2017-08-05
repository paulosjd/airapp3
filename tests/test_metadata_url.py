from unittest import TestCase
from views.charts import get_metadata_url


class TestGet_urls(TestCase):

    def setUp(self):
        self.expected_url = 'http://api.erg.kcl.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode=MY1/json'

    def test_get_urls(self):
        url = get_metadata_url('MY1')
        self.assertEqual(url, self.expected_url)


if __name__ == '__main__':
    unittest.main()