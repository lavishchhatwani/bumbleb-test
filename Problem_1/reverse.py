import sys
import os
import random


# Get the absolute path of the parent directory (bumbleb-test)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import comman
from comman import execution_time

@execution_time
def reverseTecnique_1(input):
    return " ".join(input.split()[::-1])
print(reverseTecnique_1("code to love I"))


@execution_time
def reverseTecnique_2(input):
    words = input.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return " ".join(reversed_words)
print(reverseTecnique_2("code to love I"))



