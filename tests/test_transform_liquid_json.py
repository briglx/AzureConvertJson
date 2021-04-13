"""Test liquid templates."""
import json

import pytest

from tests import LOGIC_APP_SOURCE_FILE, TEMPLATE_PATH
from transform.liquid_json_transform import (
    convert_quality_filter,
    generate_guid,
    render_dict,
)


def test_quality_filter():
    """Test quality filter for template."""
    assert convert_quality_filter("A01") == "Poor"
    assert convert_quality_filter("A04") == "Good"


def test_quality_filter_error():
    """Test quality filter for template."""
    with pytest.raises(ValueError):
        convert_quality_filter("BadValue")


def test_transform_from_to_data():
    """Test Transforming source to target"""
    # template_name = os.path.join("docs", "template_transform.liquid.json")
    # template_path = "transform"
    with open(LOGIC_APP_SOURCE_FILE, "r") as template_file:
        text = template_file.read()
        data = json.loads(text)

    # append guid to data
    data["system_guid"] = generate_guid()

    filters = {"convert": convert_quality_filter}

    template_name = "transform_message.liquid.json"
    message = render_dict(data, TEMPLATE_PATH, template_name, filters)

    assert isinstance(message, dict)
    assert message["CreatedTime"] == "2020-11-17T06:25:12Z"
    assert len(message["Body"]["value"]["HistorySamples"]) == 2
    assert message["Body"]["value"]["HistorySamples"][0]["Value"] == 25.93
    assert message["Body"]["value"]["HistorySamples"][0]["Quality"] == "Good"
