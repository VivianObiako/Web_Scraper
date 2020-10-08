# Show examples of how you would use ALL your implementations here
from src.db import DB
from src.spider import spider_task
from decouple import config
from celery import Celery


DB.connect()
DB.new_connect()
DB.setup()
DB.seed()
# print(DB.links())
# print(DB.pages())
#
# pages = DB.pages()
# print(pages.select())
# print(pages.fetch_url(2))
# print(pages.update_false(1))
# print(pages.update_true(1))
# print(pages.find(1))


# links = DB.links()
# print(links.insert(2, 'https://rb.gy/zd2xxz',))
# print(links.insert(1, 'https://rb.gy/zd2xxz',))
# print(links.select())
# print(links.delete(2))
# print(links.select())
# print((spider_task(1)))

# celery task
# app = Celery('main', broker=config('CELERY_BROKER'), backend=config('CELERY_BACKEND'))
#
# @app.task
# def test():
#   return spider_task(2)





