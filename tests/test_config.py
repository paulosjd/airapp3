import unittest
from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        tester = app.test_client(self)
        self.response = tester.get('http://localhost:8080/chart/index')

    def test_sum(self):
        self.assertEqual(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
