from unittest import TestCase
from views.charts import get_json_url
import re

class TestGet_urls(TestCase):

    def setUp(self):
        url_1 = get_json_url('MY1', 3)
        url_2 = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=21%20Jul%202017/' \
                'EndDate=24%20Jul%202017/Json'
        self.url_1 = (re.sub('[0-9]','1', url_1)
        self.url_2 = (re.sub('[0-9]','1', url_1)


    def test_get_urls(self):
        url = get_json_url('MY1', 3)
        self.assertEqual(url.status_code, 200)




s3 = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=11%11Jul%111111/' \
                            'EndDate=11%11Jul%111111/Json'

s2=(re.sub('[0-9]','1', s1))

if s2==s3:
    print(3)