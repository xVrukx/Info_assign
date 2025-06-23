from assign_a_test_logic import priem_test


def test_default():
    assert priem_test() == 'addition of prim numbers is 17'

def test_range():
    assert priem_test(10, 20) == 'addition of prim numbers is 60'

def test_invalid():
    assert priem_test(20, 10) == 'please enter numbers  and second number should be > than first'
