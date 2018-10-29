# "Database code" for the DB Forum.

import psycopg2

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database="forum")
  c = db.cursor()
  query = "select content, time from posts order by time desc;"
  c.execute(query)
  posts = c.fetchall()
  db.close()
  return posts
  

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database="forum")
  c = db.cursor()
  c.execute("insert into posts values (%s)",(content,))
  db.commit()
  db.close()


