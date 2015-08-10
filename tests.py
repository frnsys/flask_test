import unittest
from app import create_app

test_config = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'
}


class MyTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(**test_config)
        self.client = self.app.test_client()

    def tearDown(self):
        self.app = None

    def test_index(self):
        resp = self.client.get('/')
        self.assertEquals(resp.data, b'sup')
        self.assertEquals(resp.status_code, 200)

    def test_404(self):
        resp = self.client.get('/doesnt_exist')
        self.assertEquals(resp.data, b'uh oh 404')
        self.assertEquals(resp.status_code, 404)