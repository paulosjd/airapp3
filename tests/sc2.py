import unittest
import json
from views.charts import get_data





get_data_dict = get_data('MY1', 3)


length_dict = {key: len(value) for key, value in get_data_dict.items()}
hours_len = length_dict['hours']
no2_len = length_dict['no2']
print(hours_len)
print(no2_len)

json_data2 = open('mock_data/my1_dict.json')
my1_dict = json.load(json_data2)

"""
get_data_dict = get_data('MY1', 3)
get_data_dict.update((k, '1') for k, v in get_data_dict.items())



print (get_data_dict )"""
#{'no2': '1', 'pm1': '1', 'pm2': '1', 'hours': '1'}

