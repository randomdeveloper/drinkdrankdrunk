import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from current_session import set_current_user

class Register(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("views/register.html", {}))
        
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")

        # todo: add validation
        user = User()
        user.email = email
        # todo: hash password
        user.password = password

        # save new user
        user.put()

        # put him into session
        set_current_user(user)

        # redirect to the home page
        self.redirect("/")        
