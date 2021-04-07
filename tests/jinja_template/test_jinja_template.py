"""Test jinja templates."""
from script import template
import os

TEST_ROOT = "tests"
TEMPLATE_PATH = os.path.join(TEST_ROOT, "jinja_template")

def test_json_nested_data():
    """Test Transforming source to target"""
    source_file_name = "source.json"
    source_file = os.path.join(TEMPLATE_PATH, source_file_name)

    template_name = "transform.json"
    
    data = template.load_data(source_file)
    message = template.convert_json(data, TEMPLATE_PATH, template_name)

    assert type(message) == dict
    assert message['CreatedTime'] == '2020-11-17T06:25:12Z'
    assert message['Body']['value']['HistorySamples'][0]['Value'] == 25.93
