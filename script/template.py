"""Json to Json Conversion using jinja templates."""
import json

from jinja2 import Environment, FileSystemLoader


def load_data(filename):
    """Load source file."""
    with open(filename, "r") as myfile:
        text = myfile.read()
    data = json.loads(text)
    return data


def save_data(data, filename):
    """Save data to json file."""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2, separators=(",", ": "))


def render(data, template_path, template_name):
    """Render data as a string for a given template."""
    # Load Environment
    loader = FileSystemLoader(template_path)
    env = Environment(loader=loader)

    # Get Template
    template = env.get_template(template_name)

    # Transform
    result_string = template.render(data)

    return result_string


def render_dict(data, template_path, template_name):
    """Render data as Json Dictionary for a given template."""
    result_string = render(data, template_path, template_name)

    return json.loads(result_string)


def render_json(data, template_path, template_name):
    """Render data as Json for a given template."""
    result_dict = render_dict(data, template_path, template_name)
    return json.dumps(result_dict)
