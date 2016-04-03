from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("hello-cloud", "templates"))
template = env.get_template("index.html")
