from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from current_session import delete_session

from models.users import User

class Signout(webapp.RequestHandler):
    def get(self):
        delete_session()
        self.redirect("/")
        
        
