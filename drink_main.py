import logging, os

# Google App Engine imports.
from google.appengine.ext.webapp import util

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        template_args={}
        self.response.out.write(template.render(path, template_args))
        user = users.get_current_user()

#		if user:
#			self.response.headers['Content-Type'] = 'text/plain'
#			self.response.out.write('Hello, ' + user.user_id())
#		else:
#			self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication(
                                    [('/', MainPage)],
                                     debug=True)
def main():
    run_wsgi_app(application)
	
if __name__ == "__main__":
    main()			
