from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        print(freq)

        for key, val in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            if key == val:
                return key

        return -1
