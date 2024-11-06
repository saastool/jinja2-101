# 1. Import the necessary libraries and components (objects, functions, etc.) from libraries.
from jinja2 import Environment, FileSystemLoader, Template

# 2. Create a jinja rendering environment and store it in a variable. This environment will be used in further steps.
env = Environment(loader = FileSystemLoader('template'))
# 3. Load the template (which stored in templates) in a variable.
template = env.get_template('_template.jinja')

# 4. Render the template using <template-object>.render() function to obtain text.
output = template.render()

# 5. Print the rendered text to the screen or a file as suitable and output into file in the renders folder.
print(output)

with open("renders/_output.txt", 'w') as f:
    print(output, file = f)