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
        username = self.request.get("user_name")
        password = self.request.get("password")
        confirm_password = self.request.get("confirm_password")
        email = self.request.get("email")
        
        model = RegisterModel()
        model.user_name = username
        model.email = email
        model.password = password
        model.confirm_password = confirm_password

        # validate data
        if not model.validate():
            # on error, redisplay form with error messages
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
    password = ""
    confirm_password = ""

    user_name_empty = False
    email_invalid = False
    password_empty = False
    passwords_dont_match = False

    def validate(self):
        self.user_name_empty = (self.user_name == "")
        # todo: email validation (user@domain etc..)
        self.email_invalid = (self.email == "")
        self.password_empty = (self.password == "")
        self.passwords_dont_match = (self.password != self.confirm_password)

        return self.is_valid()

    def is_valid(self):
        return not(self.user_name_empty or self.email_invalid\
               or self.password_empty or self.passwords_dont_match)
