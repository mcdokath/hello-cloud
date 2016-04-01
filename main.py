# Author: Kathryn McDonald
# Creation Date: 3/31/2016
# Source: https://cloud.google.com/appengine/docs/python/

import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = "text/plain"
		self.response.write("Hello, World!")

app = webapp2.WSGIApplication([
	("/", MainPage),
], debug=True)
