<<<<<<< HEAD
"""Template with String engine."""
import os
from string import Template

=======

"""Json to Json Conversion using string templates."""
import os

from string import Template
>>>>>>> faf9031... Reorg Tests. Add liquid.

def render(data, template_path, template_name):
    """Render data as a string for a given template."""
    file_name = os.path.join(template_path, template_name)
<<<<<<< HEAD

    with open(file_name, "r") as template_file:
        template = Template(template_file.read())

    # Transform
    result_string = template.substitute(data)

    return result_string
=======
    
    with open(file_name, "r") as template_file:
        template = Template(template_file.read())
    
    # Transform
    result_string = template.substitute(data)
    
    return result_string
>>>>>>> faf9031... Reorg Tests. Add liquid.
