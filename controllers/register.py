import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from current_session import set_current_user
from request_model_binder import model_from_request
from models.users import User

class Register(webapp.RequestHandler):
    def get(self):
        model = RegisterModel()
        self.view(model)
    
    def post(self):
        model = model_from_request(self.request, RegisterModel)

        # validate data
        if not model.validate():
            # on error, redisplay form with error messages
            self.view(model)
            return

        # save new user        
        user = User()
        user.username = model.user_name
        user.email = model.email
        # todo: hash password
        user.password = model.password

        user.put()

        # put him into session
        set_current_user(user)

        # redirect to the home page
        self.redirect("/")

    def view(self, model):
        self.response.out.write(template.render("views/register.html", {"model": model}))

        
class RegisterModel:  
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
