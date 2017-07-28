import unittest
import json
from views.charts import get_json


json_data = open('mock_data/my1_data.json')
data = json.load(json_data)
my1_array = data['AirQualityData']['Data']


class TestCase(unittest.TestCase):
    
    # Change values to allow for different dates    
    def setUp(self):        
        get_json_array = get_json('MY1', 3)
        for d in get_json_array:
            for value in d:
                d[value] = '1'        
        for d in my1_array:            
            for value in d:
                d[value] = '1'        
        self.data1 = get_json_array        
        self.data2 = my1_array

    def test_list_of_dicts_structure(self):
        self.assertEqual(self.data1, self.data2)


if __name__ == '__main__':
    unittest.main()
