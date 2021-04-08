"""Test main functions."""
from datetime import datetime

from script import main


def test_iso_date():
    """Test iso date."""

    test_date = datetime(2021, 1, 1, 5, 30, 0)
    iso_date = main.get_date_isoformat(test_date)
    assert iso_date == "2021-01-01T05:30:00Z"


def test_generate_id():
    """Test generate id."""

    test_id = main.generate_id()

    assert len(test_id) == 32
    assert int(test_id, 16)
