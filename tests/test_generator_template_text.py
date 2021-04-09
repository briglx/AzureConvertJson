"""Test templates."""
from generator.python_generator import template_string
from tests import SAMPLE_DATA, TEMPLATE_PATH, TEST_RESOURCE_PATH

def test_simple_template():
    """Test simple template."""

    template_name = "simple_template.txt"
    message = template_string.render(SAMPLE_DATA, TEST_RESOURCE_PATH, template_name)
    
    assert message == "m_rid=232b010507bcb07c33ba27a6f636f64c"


def test_multiline_template():
    """Test multiline template."""

    template_name = "multiline_template.txt"
    message = template_string.render(SAMPLE_DATA, TEST_RESOURCE_PATH, template_name)

    assert (
        message
        == "m_rid=232b010507bcb07c33ba27a6f636f64c\ncreatedDateTime=2020-11-18T06:25:12Z"
    )
