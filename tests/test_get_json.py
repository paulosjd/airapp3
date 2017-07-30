import unittest
import json
from views.charts import get_json


"""get_json should with a list of dicts as follows:
   [{'@MeasurementDateGMT': '...', '@SpeciesCode': '...', '@Value': '...'},
    ...., {'@MeasurementDateGMT': '...', '@SpeciesCode': '...', '@Value': '...'}]"""

json_data = open('mock_data/my1_data.json')
data = json.load(json_data)
my1_array = data['AirQualityData']['Data']


class TestCase(unittest.TestCase):

    # Change values to allow for different dates
    def setUp(self):
        get_json_array = get_json('MY1', 3)
        for d in get_json_array:
            d.update((k, '1') for k, v in d.items())
        for d in my1_array:
            d.update((k, '1') for k, v in d.items())
        self.data1 = get_json_array[0]
        self.data2 = my1_array[0]

    def test_list_of_dicts_structure(self):
        self.assertEqual(self.data1, self.data2)


if __name__ == '__main__':
    unittest.main()

