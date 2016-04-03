import time
import jinja2

# create output string
output = "Current time: {{ timeobj.strftime('%H:%M') }}"
print(output)

# put output string into jinja
jOutput = jinja2.Template(output)
print(jOutput.render(timeobj = time))
