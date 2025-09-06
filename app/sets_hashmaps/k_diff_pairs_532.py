from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        seen = set(nums)

        if k > 0:
            for num in seen:  # b - a = k => b = a + k
                if num + k in seen:
                    count += 1
        else:
            freq = Counter(nums)
            for num in freq:
                if freq[num] > 1:
                    count += 1

        return count