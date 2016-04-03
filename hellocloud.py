import time
import jinja2
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello Cloud!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
