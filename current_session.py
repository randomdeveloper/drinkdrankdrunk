
from appengine_utilities.sessions import Session

from models.users import User

session_key = "current_user"

def current_user():
  session = Session()
  if session.has_key(session_key):
    return session[session_key]
  else:
    return None
  
def set_current_user(user):
  session = Session()
  session[session_key] = user