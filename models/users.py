
from google.appengine.ext import db

class User(db.Model):
    # TODO: Let's add username and authenticate on it instead of email
    email = db.EmailProperty()
    password = db.StringProperty()
    
