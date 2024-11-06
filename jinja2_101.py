from jinja2 import Template

f = open("jinja_template.jinja", "r")

template = Template(f.readline())
f.close()

output = template.render()
print(output)