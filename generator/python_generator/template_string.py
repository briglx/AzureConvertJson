"""Json to Json Conversion using string templates."""
import os
from string import Template


def render(data, template_path, template_name):
    """Render data as a string for a given template."""
    file_name = os.path.join(template_path, template_name)

    with open(file_name, "r") as template_file:
        template = Template(template_file.read())

    # Transform
    result_string = template.substitute(data)

    return result_string
