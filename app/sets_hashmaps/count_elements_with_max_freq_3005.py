from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = float('-inf')

        for num in freq:
            max_freq = max(max_freq, freq[num])

        summ_max_freq = 0

        for num in freq:
            if freq[num] == max_freq:
                summ_max_freq += freq[num]

        return summ_max_freq
