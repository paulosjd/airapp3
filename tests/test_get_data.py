import unittest
import json
from views.charts import get_data


"""get_data() should return a dictionary with the following structure:
{'hours': ['00:00', '01:00', ..... '23:00'],
 'no2': [41.7,.... 53.2],
 'pm1': [22.9,.....24.3],
 'pm2': ['', .... '', '']}"""


json_data2 = open('mock_data/my1_dict.json')
my1_dict = json.load(json_data2)


class TestCase(unittest.TestCase):

    # Change values to allow for different dates, except for datetime values to test values assigned to hours variable
    def setUp(self):
        get_data_dict = get_data('MY1', 3)
        for d in get_data_dict:
            d.update((k, '1') for k, v in d.items() if k == '@Value' and v != 'hours')
        for d in my1_dict:
            d.update((k, '1') for k, v in d.items() if k == '@Value' and v != 'hours')
        self.data1 = get_data_dict
        self.data2 = my1_dict

    def test_dict_structure(self):
        self.assertEqual(self.data1, self.data2)


if __name__ == '__main__':
    unittest.main()








