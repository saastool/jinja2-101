from jinja2 import Environment, FileSystemLoader, Template

env = Environment(loader = FileSystemLoader('template'))
template = env.get_template('variables_template.jinja')

output = template.render(name = 'World')

print(output)

with open("renders/variables_output.txt", 'w') as f:
    print(output, file = f)