
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from current_session import current_user, set_current_user
from models.users import User

class MainPage(webapp.RequestHandler):
    def get(self):
        model = {}
        
        user = current_user()
        if user:
            model["user_name"] = user.username
        self.response.out.write(template.render('views/index.html', model))

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
