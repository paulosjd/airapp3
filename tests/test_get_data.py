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

    # Test that lengths of dictionary values are correct

    get_data_dict = get_data('MY1', 3)

    length_dict_1 = {key: len(value) for key, value in get_data_dict.items()}
    hours_len_1 = length_dict_1['hours']
    no2_len_1 = length_dict_1['no2']
    print(hours_len_1)
    print(no2_len_1)

    length_dict_2 = {key: len(value) for key, value in my1_dict.items()}
    hours_len_2 = length_dict_2['hours']
    no2_len_2 = length_dict_2['no2']
    print(hours_len_2)
    print(no2_len_2)

    def setUp(self):
        get_data_dict = get_data('MY1', 3)
        length_dict_1 = {key: len(value) for key, value in get_data_dict.items()}
        length_dict_2 = {key: len(value) for key, value in my1_dict.items()}
        self.hours_len_1 = length_dict_1['hours']
        self.no2_len_1 = length_dict_1['no2']
        self.hours_len_2 = length_dict_2['hours']
        self.no2_len_2 = length_dict_2['no2']


    def test_hours_length(self):
        self.assertEqual(self.hours_len_1, self.hours_len_2)

    def test_no2_length(self):
        self.assertEqual(self.no2_len_1, self.no2_len_2)


if __name__ == '__main__':
    unittest.main()








