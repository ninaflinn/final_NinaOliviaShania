from app.my_mod import enlarge

def test_example():
    assert 2+2 == 4

def test_enlarge():
    assert enlarge(10) == 1000
