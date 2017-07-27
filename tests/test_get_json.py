import unittestimport json
from views.charts 
import get_json


json_data = open('mock_data/my1_data.json')
data = json.load(json_data)
my1_array = data['AirQualityData']['Data']


class TestCase(unittest.TestCase):        
# Change values to allow for different dates    
    def setUp(self):        
        get_json_array = get_json('MY1', 3)        
        for d in my1_array:            
            for value in d:                
            d[value] = '1'
    
    def test_dict_structure(self):                       
        self.AssertEqual(self.get_json_array, self.my1_array)
