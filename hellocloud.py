import time
import jinja2
import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    
    # create output string
    output = "Current time: {{ timeobj.strftime('%H:%M') }}"

    # put output string into jinja
    jOutput = jinja2.Template(output)
    self.response.write(jOutput.render(timeobj = time))

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
