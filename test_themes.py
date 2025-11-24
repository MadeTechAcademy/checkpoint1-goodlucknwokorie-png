from themes import duties

def test_all_duties():
    assert len(duties) == 13
     assert len(duties) == 13, f"Expected 13 duties, found {len(duties)}"

    # Check no duplicates
    assert len(duties) == len(set(duties)), "Duplicate duties found!"

    # Check each duty starts with the correct number
    for i, duty in enumerate(duties, start=1):
        assert duty.startswith(f"Duty {i}"), f"Duty {i} is incorrect: {duty}"

