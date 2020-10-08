import unittest
from src.db import DB
from src.db.pages import Pages


class TestPages(unittest.TestCase):
  '''class that tests Pages class'''

  def setUp(self):
    '''function that sets up for testing '''
    self.pages = Pages(DB.new_connect())

  def test_select(self):
    '''function that tests the select function'''
    DB().setup()
    DB().seed()
    result = [(1, 'https://www.facebook.com'), (2, 'https://rb.gy/zd2xxz')]
    self.assertEqual(self.pages.select(), result)

  def test_fetch_url(self):
    '''function that tests the fetch_url function'''
    DB().setup()
    DB().seed()
    result = ('https://rb.gy/zd2xxz',)
    self.assertEqual(self.pages.fetch_url(2), result)

  def test_find(self):
    '''function that tests the find function'''
    DB().setup()
    DB().seed()
    result = (1, 'https://www.facebook.com')
    self.assertEqual(self.pages.find(1)[:2], result)

  def test_update_true(self):
    '''function that tests the update_true function'''
    DB().setup()
    DB().seed()
    result = (1, 'https://www.facebook.com', True)
    self.assertEqual(self.pages.update_true(1)[:3], result)

  def test_update_false(self):
    '''function that tests the update_false function'''
    DB().setup()
    DB().seed()
    result = (1, 'https://www.facebook.com', False)
    self.assertEqual(self.pages.update_false(1)[:3], result)

  def tearDown(self):
    self.pages = None

if __name__ == '__main__':
    unittest.main()