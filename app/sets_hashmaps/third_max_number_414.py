from collections import Counter
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        count_dict = Counter(nums)

        if len(count_dict) < 3:
            return max(nums)

        i = 0
        third_max = float('inf')
        for key in sorted(count_dict, reverse = True):
            if i == 3:
                break
            third_max = min(third_max, key)
            i += 1

        print(third_max)
        return third_max