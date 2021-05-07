"""Test temperature templates."""
import json
from liquid import Liquid, filter_manager
import os
from tests import TEST_RESOURCE_PATH
import datetime

import pytest


def parse_epoch_time(epoch_time, date_format):
    ts = datetime.datetime.fromtimestamp(epoch_time)
    return ts.strftime(date_format)


def test_temp_transform():

    # Add custom filter
    filter_manager.register("epoch")(parse_epoch_time)

    # Get Data
    data_file_name = "source_temp_message.json"
    data_file_path = os.path.join(TEST_RESOURCE_PATH, data_file_name)
    with open(data_file_path, "r") as data_file:
        data_text = data_file.read()
    data = json.loads(data_text)
    
    # Get Template
    template_name = "transform_temp_template.liquid.json"
    template_file_name = os.path.join(TEST_RESOURCE_PATH, template_name)
    with open(template_file_name, "r") as template_file:
        template_string = template_file.read()
    template = Liquid(template_string)

    # Transform
    result_string = template.render(**data)  # Unpack argument lists

    assert result_string == "signify spaceId: 60a490be-6e77-4bcf-8c0e-6200b9e16cb9, humidity 57, time 2021-05-07T11:47:38Z,Poor"


test_temp_transform()