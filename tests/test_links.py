import unittest
from src.db import DB
from src.db.links import Links


class TestLinks(unittest.TestCase):
  '''class that tests Pages class'''

  def setUp(self):
    '''function that sets up for testing '''
    self.links = Links(DB.new_connect())

  def test_insert(self):
    '''function that tests the insert function'''
    DB().setup()
    DB.seed()
    self.assertEqual(self.links.insert(2, 'https://www.google.com'), None)

  def test_select(self):
    '''function that tests the select function'''
    DB().setup()
    DB.seed()
    self.links.insert(2, 'https://www.google.com')
    result = [(2, 'https://www.google.com')]
    self.assertEqual(self.links.select(), result)

  def test_delete(self):
    '''function that tests the delete function'''
    DB().setup()
    DB.seed()
    self.links.insert(2, 'https://www.google.com')
    self.links.delete(2)
    self.assertEqual(self.links.select(), [])

  def tearDown(self):
    self.links = None

if __name__ == '__main__':
    unittest.main()