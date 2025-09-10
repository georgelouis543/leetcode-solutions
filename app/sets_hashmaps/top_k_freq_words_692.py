from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        print(words)
        count_word_dict = Counter(words)
        freq = [[] for i in range(0, len(words) + 1)]
        res = []

        for key in count_word_dict:
            freq[count_word_dict[key]].append(key)

        print(freq)

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res
