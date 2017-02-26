import unittest
from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        tester = app.test_client(self)
        self.response = tester.get('/')

    def test_sum(self):
        self.assertEquals(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()


"""
    def setUp(self):
        self.data = {"AirQualityData": {"@SiteCode": "MY1",
                     "Data": [{"@SpeciesCode": "NO2","@MeasurementDateGMT": "2017-02-19 11:00:00", "@Value": "91.1"},
                              {"@SpeciesCode": "NO2","@MeasurementDateGMT": "2017-02-19 12:00:00", "@Value": "93.6"},
                              {"@SpeciesCode": "NO2","@MeasurementDateGMT": "2017-02-19 13:00:00", "@Value": "106.5"}]}}
    def setUp(self):
        self.data = {"AirQualityData": {
                "@SiteCode": "MY1",
                "Data": [{"@SpeciesCode": "CO", "@MeasurementDateGMT": "2017-02-19 00:00:00", "@Value":"0.8"},
                         {"@SpeciesCode": "CO", "@MeasurementDateGMT": "2017-02-19 01:00:00", "@Value":"0.6"},
                         {"@SpeciesCode": "CO", "@MeasurementDateGMT": "2017-02-19 02:00:00", "@Value":"0.4"},
                         {"@SpeciesCode": "CO", "@MeasurementDateGMT": "2017-02-19 03:00:00", "@Value":"0.5"}]}}
        self.array = [{'@Value': '0.8', '@MeasurementDateGMT': '2017-02-19 00:00:00', '@SpeciesCode': 'CO'},
                 {'@Value': '0.6', '@MeasurementDateGMT': '2017-02-19 01:00:00', '@SpeciesCode': 'CO'},
                 {'@Value': '0.4', '@MeasurementDateGMT': '2017-02-19 02:00:00', '@SpeciesCode': 'CO'},
                 {'@Value': '0.5', '@MeasurementDateGMT': '2017-02-19 03:00:00', '@SpeciesCode': 'CO'}]
        self.co = [0.8, 0.6, 0.4, 0.5]

class TestGet_urls(TestCase):

    def setUp(self):
        self.expected_urls = ['http://international.o2.co.uk/internationaltariffs/getintlcallcosts?countryId=CAN',
                              'http://international.o2.co.uk/internationaltariffs/getintlcallcosts?countryId=DEU',
                              'http://international.o2.co.uk/internationaltariffs/getintlcallcosts?countryId=ISL',
                              'http://international.o2.co.uk/internationaltariffs/getintlcallcosts?countryId=PAK',
                              'http://international.o2.co.uk/internationaltariffs/getintlcallcosts?countryId=SGP',
                              'http://international.o2.co.uk/internationaltariffs/getintlcallcosts?countryId=ZAF']

    def test_get_urls(self):
        urls = get_urls()
self.assertEqual(urls, self.expected_urls)"""