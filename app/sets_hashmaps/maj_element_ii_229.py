from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count_dict = Counter(nums)
        n = len(nums)

        for key in count_dict:
            if count_dict[key] > n // 3:
                res.append(key)

        return res
