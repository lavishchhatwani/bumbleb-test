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
def get_anagrams_good_practice(strs):
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

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(get_anagrams_good_practice(strs))


@execution_time
def get_anagrams_bad_practice(strs):
    if not all(check_constraints(strs)):  
        print("""Constraints:
            1 <= strs.length <= 104
            0 <= strs[i].length <= 100
            strs[i] consists of lowercase English letters.""")
        return []

    anagrams = defaultdict(list)

    for word in strs:
        lower_case_word = word.lower()

        # DUE TO BELOW STEPS ITS USING MORE MEMORY WE SHOULD TAKE CARE OF THIS SMALL THINGS.
        # STEP 1
        sorted_word = tuple(sorted(lower_case_word))
        sorted_word = tuple(sorted(list(sorted_word)))

        # STEP 2
        if sorted_word in anagrams:
            anagrams[sorted_word].append(lower_case_word)
        else:
            anagrams[sorted_word] = []
            anagrams[sorted_word].append(lower_case_word)

        # STEP 2
        temp_list = list(sorted_word)  # Converting tuple to list
        temp_list = tuple(temp_list)   # Converting back to tuple (useless operation)

    return [anagrams[key] for key in anagrams.keys()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(get_anagrams_bad_practice(strs))
