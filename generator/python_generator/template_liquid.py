"""Template with Liquid engine."""
import json
import os

from liquid import Liquid


def render(data, template_path, template_name, debug=False):
    """Render data as a string for a given template."""
    file_name = os.path.join(template_path, template_name)

    with open(file_name, "r") as template_file:
        template_string = template_file.read()
    template = Liquid(template_string, liquid_config={"debug": debug})

    # Transform
    result_string = template.render(**data)  # Unpack argument lists

    return result_string


def render_dict(data, template_path, template_name):
    """Render data as Json Dictionary for a given template."""
    result_string = render(data, template_path, template_name)

    return json.loads(result_string)
