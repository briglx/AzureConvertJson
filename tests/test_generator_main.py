"""Test main functions."""
from datetime import datetime

from generator.python_generator import main


def test_iso_date():
    """Test iso date."""

    test_date = datetime(2021, 1, 1, 5, 30, 0)
    iso_date = main.get_date_isoformat(test_date)
    assert iso_date == "2021-01-01T05:30:00Z"

<<<<<<< HEAD

=======
>>>>>>> faf9031... Reorg Tests. Add liquid.
def test_generate_id():
    """Test generate id."""

    test_id = main.generate_id()

    assert len(test_id) == 32
<<<<<<< HEAD
    assert int(test_id, 16)
=======
    assert int(test_id, 16)
>>>>>>> faf9031... Reorg Tests. Add liquid.
