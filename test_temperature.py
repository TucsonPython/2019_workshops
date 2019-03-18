"""
pytest -v
"""
import temperature

def test_fahr_to_celsius():
    expected_out = 100
    actual_out = temperature.fahr_to_celsius(212)
    assert actual_out == expected_out
