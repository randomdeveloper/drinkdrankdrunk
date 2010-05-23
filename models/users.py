
from google.appengine.ext import db

class User(db.Model):
    email = db.EmailProperty()
    password = db.StringProperty()
    
