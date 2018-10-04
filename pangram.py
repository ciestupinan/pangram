"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""
import string

def is_pangram(sentence):
	"""Given a string, return True if it is a pangram, False otherwise."""
	lowercase_sentence = sentence.lower()
	alphabet = [string.ascii_lowercase[i] for i in range(len(string.ascii_lowercase))]
	alphabet_count = {}

	for letter in alphabet:
		alphabet_count[letter] = 0

	for ch in sentence:
		if ch in alphabet_count:
			count = alphabet_count[ch]
			alphabet_count[ch] = count+1

	if 0 in alphabet_count.values():
		return False
	return True

if __name__ == "__main__":
	import doctest
	if doctest.testmod().failed == 0:
		print("\n*** ALL TESTS PASSED. YAY!\n")
