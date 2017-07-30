from unittest import TestCase
from views.charts import get_json_url


class TestGet_urls(TestCase):

    def setUp(self):
        self.expected_url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=21%20Jul%202017/' \
                            'EndDate=24%20Jul%202017/Json'

    def test_get_urls(self):
        url = get_json_url('MY1', 3)
        self.assertEqual(url.status_code, 200)

import re

s1 = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=21%20Jul%202017/' \
                            'EndDate=24%20Jul%202017/Json'
s3 = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=11%11Jul%111111/' \
                            'EndDate=11%11Jul%111111/Json'

s2=(re.sub('[0-9]','1', s1))

if s2==s3:
    print(3)