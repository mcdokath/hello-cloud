# Author: Kathryn McDonald
# Creation Date: 3/31/2016
# Source: https://cloud.google.com/appengine/docs/python/

import webapp2

MAIN_PAGE_HTML = """\
<!DOCTYPE html>
<html>
<head>
  <link href='https://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <title>Hello Cloud</title>
</head>
<body>
  <h1>Hello, Cloud!</h1>
  <p>This is a sample webpage.</p>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(MAIN_PAGE_HTML)

app = webapp2.WSGIApplication([
	("/", MainPage),
], debug=True)
