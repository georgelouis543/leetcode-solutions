from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        consonants = {"q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b",
                      "n", "m"}
        count_dict = Counter(s)
        max_consonant = 0
        max_vowel = 0

        for c in count_dict:
            if c in vowels:
                max_vowel = max(max_vowel, count_dict[c])
            if c in consonants:
                max_consonant = max(max_consonant, count_dict[c])

        print(max_consonant + max_vowel)

        return max_consonant + max_vowel
