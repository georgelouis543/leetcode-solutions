from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(word)

        print(anagrams_dict)

        return list(anagrams_dict.values())