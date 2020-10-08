class Links:
  '''class that handles links table database interface'''
  def __init__(self, connect):
    self.connection = connect
    self.cursor = self.connection.cursor()

  def insert(self, page_id, url):
    '''function that inserts all id, page_id and url into links table'''
    self.cursor.execute('''INSERT INTO links (page_id, url) VALUES (%s, %s) ''', (page_id, url))
    self.connection.commit()

  def select(self):
    '''function that selects all id and url from the `links` table'''
    self.cursor.execute('SELECT page_id,url FROM links')
    record = self.cursor.fetchall()
    return record

  def delete(self, page_id):
    '''function that deletes all values in links table'''
    self.cursor.execute(''' DELETE FROM Links where page_id=%s''', (page_id,))
    self.connection.commit()

