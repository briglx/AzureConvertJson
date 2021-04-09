"""Test liquid templates."""
import json

from generator.python_generator import main, template_liquid
from tests import SOURCE_FILE, TEMPLATE_PATH


def test_transform_from_to_data():
    """Test Transforming source to target"""
    # template_name = os.path.join("docs", "template_transform.liquid.json")
    with open(SOURCE_FILE, "r") as template_file:
        text = template_file.read()
        data = json.loads(text)

    # append guid to data
    data["system_guid"] = main.generate_guid()

    template_name = "template_transform.liquid.json"
    message = template_liquid.render_dict(data, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert message["CreatedTime"] == "2020-11-17T06:25:12Z"
    assert len(message["Body"]["value"]["HistorySamples"]) == 2
    assert message["Body"]["value"]["HistorySamples"][0]["Value"] == 25.93
    assert message["Body"]["value"]["HistorySamples"][0]["Quality"] == "A04"
