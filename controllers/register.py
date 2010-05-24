import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from current_session import set_current_user

from models.users import User

class Register(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("views/register.html", {}))
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        email = self.request.get("email")

        # todo: add validation
        user = User()
        user.username = username
        # todo: hash password
        user.password = password
        user.email = email

        # save new user
        user.put()

        # put him into session
        set_current_user(user)

        # redirect to the home page
        self.redirect("/")        
