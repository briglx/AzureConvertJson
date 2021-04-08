"""Test jinja templates."""
import os

import pytest

from generator.python_generator import template

TEST_ROOT = "tests/generator"
TEST_FILE_PATH = os.path.join(TEST_ROOT, "jinja_template")
TEMPLATE_PATH = "docs"


def test_transform_from_to_data():
    """Test Transforming source to target"""
    source_file_name = "source.json"
    source_file = os.path.join(TEST_FILE_PATH, source_file_name)

    template_name = "template_transform.json"

    data = template.load_data(source_file)
    message = template.render_dict(data, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert message["CreatedTime"] == "2020-11-17T06:25:12Z"
    assert message["Body"]["value"]["HistorySamples"][0]["Value"] == 25.93


def test_create_from_message():
    """Test generating the from message from test data."""
    sample_data = {
        "m_rid": "232b010507bcb07c33ba27a6f636f64c",
        "create_datetime": "2020-11-18T06:25:12Z",
        "period_start_time": "2021-04-06T19:02:22Z",
        "period_end_time": "2021-04-06T19:02:47Z",
        "values": [
            {
                "start_interval": "2021-04-06T19:02:22Z",
                "end_interval": "2021-04-06T19:02:23Z",
                "value": 39.8,
                "quality": "A04",
            }
        ],
    }

    template_name = "template_source_message.json"
    message = template.render_dict(sample_data, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["mRID"]
        == sample_data["m_rid"]
    )
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["createdDateTime"]
        == sample_data["create_datetime"]
    )
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["period.timeInterval"][
            "start"
        ]
        == sample_data["period_start_time"]
    )
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["period.timeInterval"][
            "end"
        ]
        == sample_data["period_end_time"]
    )
    assert len(
        message["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"]
    ) == len(sample_data["values"])


def test_create_from_message_with_filter():
    """Test generating the from message from test data."""
    sample_data = {
        "m_rid": "232b010507bcb07c33ba27a6f636f64c",
        "create_datetime": "2020-11-18T06:25:12Z",
        "period_start_time": "2021-04-06T19:02:22Z",
        "period_end_time": "2021-04-06T19:02:47Z",
        "values": [
            {
                "start_interval": "2021-04-06T19:02:22Z",
                "end_interval": "2021-04-06T19:02:23Z",
                "value": 39.8,
                "quality": "A04",
            }
        ],
    }

    template_name = "template_source_message.json"
    message = template.render_dict(sample_data, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert len(
        message["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"]
    ) == len(sample_data["values"])
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"][0]["Period"][
            0
        ]["Point"][0]["out_Quantity.quality"]
        == "Good"
    )


def test_quality_filter():
    """Test quality filter for template."""
    assert template.convert_quality_filter("A01") == "Poor"
    assert template.convert_quality_filter("A04") == "Good"


def test_quality_filter_error():
    """Test quality filter for template."""
    with pytest.raises(ValueError):
        template.convert_quality_filter("BadValue")