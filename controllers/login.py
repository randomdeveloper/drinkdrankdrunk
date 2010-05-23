from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from models.users import User

class Login(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("views/login.html", {}))
        
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")

        # load user by email and password...
        user = User.all()\
                .filter("email =", email)\
                .filter("password =", password)\
                .get()

        if user:
            self.response.out.write("OK")
        else:
            self.response.out.write("FAIL")
