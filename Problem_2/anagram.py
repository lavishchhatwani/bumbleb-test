import sys
import os

# Get the absolute path of the parent directory (bumbleb-test)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from comman import execution_time
from collections import defaultdict


def check_constraints(strs):
    constraints = []
    if len(strs) >= 1 and len(strs) <= 10**4 :
        constraints.append(True)
    else:
        constraints.append(False)
    for word in strs:
        if len(word) >= 0 and len(word) <= 100:
            constraints.append(True)
        else:
            constraints.append(False)
        if word.islower():
            constraints.append(True)
        else:
            constraints.append(False)
    return constraints

@execution_time
def get_anagrams(strs):
    
    if not all(check_constraints(strs)):  
        print("""Constraints:
            1 <= strs.length <= 104
            0 <= strs[i].length <= 100
            strs[i] consists of lowercase English letters.""")
    else:
        anagrams = defaultdict(list)
        for word in strs:
            lower_case_word = word.lower()
            sorted_word = tuple(sorted(lower_case_word))
            anagrams[sorted_word].append(lower_case_word)
        return [anagrams[anagram_key] for anagram_key in anagrams.keys()]

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat"]
print(get_anagrams(strs))