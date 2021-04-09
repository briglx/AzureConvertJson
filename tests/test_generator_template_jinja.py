"""Test jinja templates."""
import os

import pytest

from generator.python_generator import template
from tests import SAMPLE_DATA, TEST_ROOT, TEST_RESOURCE_PATH, TEMPLATE_PATH, SOURCE_FILE

def test_transform_from_to_data():
    """Test Transforming source to target"""
    # Load source data
    data = template.load_data(SOURCE_FILE)

    template_name = "template_transform.jinja.json"
    message = template.render_dict(data, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert message["CreatedTime"] == "2020-11-17T06:25:12Z"
    assert message["Body"]["value"]["HistorySamples"][0]["Value"] == 25.93


def test_create_from_message():
    """Test generating the from message from test data."""

    template_name = "template_source_message.json"
    message = template.render_dict(SAMPLE_DATA, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["mRID"]
        == SAMPLE_DATA["m_rid"]
    )
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["createdDateTime"]
        == SAMPLE_DATA["create_datetime"]
    )
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["period.timeInterval"][
            "start"
        ]
        == SAMPLE_DATA["period_start_time"]
    )
    assert (
        message["result"][0]["MyEnergyData_MarketDocument"]["period.timeInterval"][
            "end"
        ]
        == SAMPLE_DATA["period_end_time"]
    )
    assert len(
        message["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"]
    ) == len(SAMPLE_DATA["values"])


def test_create_from_message_with_filter():
    """Test generating the from message from test data."""
    template_name = "template_source_message.json"
    message = template.render_dict(SAMPLE_DATA, TEMPLATE_PATH, template_name)

    assert isinstance(message, dict)
    assert len(
        message["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"]
    ) == len(SAMPLE_DATA["values"])
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
