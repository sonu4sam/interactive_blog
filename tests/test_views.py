import unittest
from app import app

class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Interactive Blog Website!', response.data)

if __name__ == '__main__':
    unittest.main()