import pytest
from reverse import reverseTecnique_1
@pytest.mark.parametrize("input_text, expected_output", [
    ("code to love I", "I love to code"),  # Basic test case
    ("Python", "Python"),  # Single word case
    ("", ""),  # Empty string case
    ("Hello, world!", "world! Hello,"),  # Case with punctuation
    ("   code   to   love   ", "love to code"),  # Case with multiple spaces
])
def test_reverseTecnique_1(input_text, expected_output):
    assert reverseTecnique_1(input_text) == expected_output