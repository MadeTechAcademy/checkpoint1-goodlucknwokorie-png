pip install pytest
from themes import duties

def test_has_13_duties():
    assert len(duties) == 13

def test_first_duty_starts_with_duty_1():
    assert duties[0].startswith("Duty 1")

def test_last_duty_is_duty_13():
    assert duties[-1].startswith("Duty 13")
