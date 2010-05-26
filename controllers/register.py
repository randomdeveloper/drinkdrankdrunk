import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from current_session import set_current_user

from models.users import User

class Register(webapp.RequestHandler):
    def get(self):
        model = RegisterModel()
        self.view(model)

    # todo: pass form data as method parameters        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        confirm_password = self.request.get("confirm_password")
        email = self.request.get("email")

        # validate data
        model = RegisterModel()
        model.user_name_empty = (username == "")
        # todo: email validation (user@domain etc..)
        model.email_invalid = (email == "")
        model.password_empty = (password == "")
        model.passwords_dont_match = (password != confirm_password)

        # if errors, redisplay form with error markers
        if model.not_valid():
            model.user_name = username
            model.email = email
            self.view(model)
            return

        # save new user        
        user = User()
        user.username = username
        # todo: hash password
        user.password = password
        user.email = email

        user.put()

        # put him into session
        set_current_user(user)

        # redirect to the home page
        self.redirect("/")

    def view(self, model):
        self.response.out.write(template.render("views/register.html", {"model": model}))

        
class RegisterModel:
    user_name = ""
    email = ""

    user_name_empty = False
    email_invalid = False
    password_empty = False
    passwords_dont_match = False

    def not_valid(self):
        return self.user_name_empty or self.email_invalid\
               or self.password_empty or self.passwords_dont_match
