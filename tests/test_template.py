"""Test templates."""
from script import main

TEST_DATA = {
    "m_rid": "3bd56d4a8acb43f6a748231d534710e1",
    "create_datetime": "2020-11-17T06:25:12Z",
    "period_start_time": "2019-07-23T22:00:00Z",
    "period_end_time": "2020-09-30T22:00:00",
    "quantity": 25.93,
    "quality": "A04",
}


def test_simple_template():
    """Test simple template."""

    path = "tests/simple_template.txt"
    message = main.create_message(path, TEST_DATA)

    assert message == "m_rid=3bd56d4a8acb43f6a748231d534710e1"


def test_multiline_template():
    """Test multiline template."""

    path = "tests/multiline_template.txt"
    message = main.create_message(path, TEST_DATA)

    assert (
        message
        == "m_rid=3bd56d4a8acb43f6a748231d534710e1\ncreatedDateTime=2020-11-17T06:25:12Z"
    )
