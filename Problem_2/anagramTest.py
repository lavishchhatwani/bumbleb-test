import pytest
from anagram import get_anagrams

@pytest.mark.parametrize("input_list, expected_output", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    (["eat", "tea", "tan", "ate", "nat"], [['eat', 'tea', 'ate'], ['tan', 'nat']]),
    (["A", "tea", "tan", "ate", "nat"], None),
    (["a"], [["a"]]),
    ([""], None)
])
def test_get_anagrams(input_list, expected_output):
    result = get_anagrams(input_list)
    assert result == expected_output
