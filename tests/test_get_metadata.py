import unittest
from views.charts import get_metadata


class TestCase(unittest.TestCase):

    # Test that lengths of dictionary values are correct
    def setUp(self):
        self.get_metadata_dict = get_metadata('MY1')
        self.expected_dict = {'site_name': 'Westminster - Marylebone Road', 'site_type': 'Kerbside'}

    def test_get_metadata(self):
        self.assertEqual(self.get_metadata_dict, self.expected_dict)


if __name__ == '__main__':
    unittest.main()
