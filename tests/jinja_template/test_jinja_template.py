"""Test jinja templates."""
from script import template


def test_json_nested_data():
    """Test Transforming source to target"""
    template_path = "tests/jinja_template"
    template_name = "transform.json"
    data = template.load_data("source.json")
    message = template.convert_json(data, template_path, template_name)

    assert type(message) == dict
