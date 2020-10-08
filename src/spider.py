import requests
from src.db import DB
from bs4 import BeautifulSoup


def spider_task(page_id):
  '''parameter page_id(int)
    fuction that receives a page_id and populates the links table
  '''

  # fetching the page url with the id provided and raises exception if url is invalid
  page_ids = [i[0] for i in DB().pages().select()]
  if page_id in page_ids:
    url = DB().pages().fetch_url(page_id)
  else:
    raise ValueError('Page_id is invalid')

  # updates the page’s is_scraping attribute to true
  DB.pages().update_true(page_id)
  print(url[0])

  # fetching the HTML content at the page url
  page = requests.get(url[0])

  # Parsing the fetched HTML content to extract hyperlinks(maximum 10)
  links = []
  soup = BeautifulSoup(page.text, features='html.parser')
  for link in soup.find_all('a', href=True):
    if 'https' in link['href']:
      links.append(link['href'])
  links = links[:10]

  # Deletes existing links that may have been previously saved for the page
  DB().links().delete(page_id)

  #Saves the newly extracted links to the database for the page
  for link in links:
    DB().links().insert(page_id, link)

  # Updates the page’s is_scraping attribute to false
  DB.pages().update_false(page_id)












