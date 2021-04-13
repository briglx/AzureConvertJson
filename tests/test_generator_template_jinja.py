"""Test jinja templates."""
from generator.python_generator import template_jinja as template
from tests import SAMPLE_DATA, TEMPLATE_PATH
import os
import pytest



def test_create_source_message():
    """Test generating the source message from test data."""

    template_name = "source_message_template.jinja.json"
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
