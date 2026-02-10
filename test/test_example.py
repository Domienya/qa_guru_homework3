import pytest

@pytest.mark.first
def test_first():
    assert 1+2 == 3
@pytest.mark.second
def test_second():
    assert len('hello') == 5

