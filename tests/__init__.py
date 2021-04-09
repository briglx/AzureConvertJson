"""Tests for Generators."""
import os
<<<<<<< HEAD

=======
>>>>>>> faf9031... Reorg Tests. Add liquid.
SAMPLE_DATA = {
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
<<<<<<< HEAD
TEMPLATE_PATH = "docs"
TEST_ROOT = "tests"
TEST_RESOURCE_PATH = os.path.join(TEST_ROOT, "resources")
SOURCE_FILE = os.path.join(TEST_RESOURCE_PATH, "source_message.json")
LOGIC_APP_SOURCE_FILE = os.path.join(
    TEST_RESOURCE_PATH, "source_logic_app_message.json"
)
=======
TEST_ROOT = "tests"
TEST_RESOURCE_PATH = os.path.join(TEST_ROOT, "resources")
TEMPLATE_PATH = "docs"
SOURCE_FILE = os.path.join(TEST_RESOURCE_PATH, "source.json")
>>>>>>> faf9031... Reorg Tests. Add liquid.
