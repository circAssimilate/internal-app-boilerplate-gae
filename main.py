import os
import webapp2
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.api import users

import functions as app_functions
import models as app_models

CONFIG = app_functions.yaml_fetcher('config')
CREDENTIALS = app_functions.yaml_fetcher('credentials')


class Main(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    user = users.get_current_user()
    is_allowed_user = app_functions.is_allowed_user(user.email())

    if not is_allowed_user:
        self.error(403)
        self.response.write('Access Denied')
        return

    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'src/client/index.html')
    self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([
  ('/', Main),
], debug=True)
