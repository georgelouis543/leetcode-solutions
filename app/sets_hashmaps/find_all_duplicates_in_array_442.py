from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        count_dict = Counter(nums)

        for key in count_dict:
            if count_dict[key] > 1:
                res.append(key)

        return res
