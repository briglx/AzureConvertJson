"""Test jinja templates."""
import json
import os

from jinja2 import Environment, FileSystemLoader


def load_data(filename):
    """Load source file."""
    source_path = os.path.join("tests", "jinja_template", filename)
    with open(source_path, "r") as myfile:
        text = myfile.read()
    data = json.loads(text)
    return data


def save_data(data):
    """Save data to json file."""
    save_path = os.path.join("tests", "jinja_template", "rendered.json")
    with open(save_path, "w") as json_file:
        json.dump(data, json_file, indent=2, separators=(",", ": "))


def test_json_nested_data():
    """Test Transforming source to target"""

    loader = FileSystemLoader("tests/jinja_template")
    env = Environment(loader=loader)

    filename = "transform.json"
    template = env.get_template(filename)

    data = load_data("source.json")
    message = template.render(data)

    save_data(message)
    # save_data(json.loads(message))
    assert True

test_json_nested_data()
