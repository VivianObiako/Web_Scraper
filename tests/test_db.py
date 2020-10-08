import unittest
from src.db import DB
from src.db.pages import Pages


class TestDb(unittest.TestCase):
  '''class that tests db class in __init__.py'''

  def setUp(self):
    '''function that sets up for testing '''
    self.db = DB()

  def test_connect(self):
    '''function that tests the connect function'''
    connection_object = self.db.connect()
    self.assertIsNotNone(connection_object)

  def test_new_connect(self):
    '''function that tests the new_connect function'''
    connection_object = self.db.new_connect()
    self.assertIsNotNone(connection_object)

  def test_setup(self):
    '''function that tests the setup function'''
    self.assertEqual(self.db.setup(), None)

  def test_seed(self):
    '''function that tests the seed function'''
    self.db.new_connect()
    self.db.setup()
    self.assertEqual(self.db.seed(), None)

  def test_links(self):
    '''function that tests the seed function'''
    self.assertIsNotNone(self.db.links())

  def test_pages(self):
    '''function that tests the seed function'''
    self.assertIsNotNone(self.db.pages())

  def tearDown(self):
    self.db = None

if __name__ == '__main__':
    unittest.main()