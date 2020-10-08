import unittest
from src.spider import spider_task
from src.db.pages import Pages


class TestSpider(unittest.TestCase):
  '''class that handles test for spider_task'''

  def test_spider_task(self):
    '''easy test for spider_task'''
    self.assertIsNone(spider_task(1))

  def test_spider_task_two(self):
    '''easy test for spider_task'''
    self.assertIsNone(spider_task(2))

  def test_spider_task_three(self):
    '''medium test for spider_task'''
    with self.assertRaises(ValueError):
      self.assertEqual(spider_task(0), None)

  def test_spider_task_four(self):
    '''hard test for spider_task'''
    with self.assertRaises(ValueError):
      self.assertEqual(spider_task('1'), None)
