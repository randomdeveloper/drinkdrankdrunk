from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from current_session import set_current_user

from models.users import User

class Login(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("views/login.html", {}))
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        # load user by username and password...
        user = User.all()\
                .filter("username =", username)\
                .filter("password =", password)\
                .get()

        if user:
            set_current_user(user)
            self.redirect("/")
        else:
            # TODO: return to filled login form with error message
            self.response.out.write("FAIL")
