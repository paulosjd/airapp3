import unittest
import json
from views.charts import get_data





get_data_dict = get_data('MY1', 3)
print(len(get_data_dict.values())

'''
get_data_dict = get_data('MY1', 3)
get_data_dict.update((k, '1') for k, v in get_data_dict.items())



print (get_data_dict )
#{'no2': '1', 'pm1': '1', 'pm2': '1', 'hours': '1'}'''
