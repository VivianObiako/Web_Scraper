from decouple import config
import psycopg2
from src.db.pages import Pages
from src.db.links import Links


class DB:
  '''class that handles database'''

  @classmethod
  def connect(cls):
    '''Function that Connects to the server,
       drops database if it exists and creates database
       Returns a connection object
    '''
    try:
      print(config('POSTGRES_PASSWORD'))
      connection = psycopg2.connect(
                                    dbname=None,
                                    port=config('POSTGRES_PORT', cast=int),
                                    host=config('POSTGRES_HOST'),
                                    password=config('POSTGRES_PASSWORD'),
                                    user=config('POSTGRES_USER')
      )
      connection.autocommit = True
      cursor = connection.cursor()

      cursor.execute(f'''DROP DATABASE IF EXISTS {config("POSTGRES_DB")}''')
      cursor.execute(f'''CREATE DATABASE {config("POSTGRES_DB")}''')
      return connection
    except (Exception, psycopg2.Error) as error:
      print('Error while connecting to PostgreSQL', error)

  @classmethod
  def new_connect(cls):
    '''Function that Connects to the database,
        Returns a connection object
    '''
    # cls.connect()
    try:
      connection = psycopg2.connect(
        dbname=config('POSTGRES_DB'),
        port=config('POSTGRES_PORT', cast=int),
        host=config('POSTGRES_HOST'),
        user=config('POSTGRES_USER'),
        password=config('POSTGRES_PASSWORD')
      )
      connection.autocommit = True
      return connection
    except (Exception, psycopg2.Error) as error:
      print('Error while connecting to PostgreSQL', error)


  @classmethod
  def setup(cls):
    ''' Function that Executes the structure SQL script
    '''
    cursor = cls.new_connect().cursor()
    with open("src/schemas/structure.sql", mode='r') as sql_file:
      query_sql = sql_file.read()
      cursor.execute(query_sql)


  @classmethod
  def seed(cls):
    ''' Function that Executes the seed SQL script
    '''
    cursor = cls.new_connect().cursor()
    with open("src/schemas/seed.sql", mode='r') as sql_file:
      query_sql = sql_file.readlines()
      for line in query_sql:
        cursor.execute(line)
    cls.new_connect().commit()

  @classmethod
  def links(cls):
    '''function that Returns a reference to the links interface'''
    links = Links(cls.new_connect())
    return links

  @classmethod
  def pages(cls):
    '''Function that Returns a reference to the pages interface'''
    pages = Pages(cls.new_connect())
    return pages

