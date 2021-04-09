"""Test liquid templates."""
import os
from liquid import Liquid

TEMPLATE_PATH = "docs"

def test_transform_from_to_data():
    """Test Transforming source to target"""
    template_name = os.path.join("docs", "template_transform.liquid.json")
    with open(template_name, "r") as template_file:
        template = template_file.read()
    
    liquid = Liquid(template)
    message = liquid.render(a=1)

    assert message == "{\"fullName\": \"1\"}"
    

