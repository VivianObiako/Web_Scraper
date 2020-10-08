class Pages:
  '''class that handles pages table database interface'''
  def __init__(self, connect):
    self.connection = connect
    self.cursor = self.connection.cursor()

  def select(self):
    '''function that selects all id and url from the `pages` table'''
    self.cursor.execute('SELECT id,url FROM pages')
    record = self.cursor.fetchall()
    return record

  def fetch_url(self, page_id):
    '''
    parameter id(int)
    Function that returns the url with id supplied from the `pages` table
    return a url(string)
    '''
    self.cursor.execute('SELECT url FROM pages WHERE id=%s', (page_id,))
    url = self.cursor.fetchone()
    return url

  def find(self, id):
    '''
    parameter id(int)
    Function that returns the row with id supplied from the `pages` table
    return a url(stri
    '''
    self.cursor.execute('SELECT * FROM pages WHERE id=%s', (id,))
    record = self.cursor.fetchone()
    return record

  def update_false(self, id):
    '''
    parameter id - int
    function that Updates the is_scraping to false for the page id provided
    data provided as `params`
    '''
    self.id = id
    update_table = 'UPDATE Pages SET is_scraping = False where id = %s'
    self.cursor.execute(update_table, (id,))
    return self.find(id)

  def update_true(self, id):
    '''
    parameter id - int
    function that Updates the is_scraping to true for the page id provided
    data provided as `params`
    '''
    self.id = id
    update_table = 'UPDATE Pages SET is_scraping = True where id = %s'
    self.cursor.execute(update_table, (id,))
    return self.find(id)




