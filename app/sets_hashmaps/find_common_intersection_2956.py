from collections import Counter
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_dict1 = Counter(nums1)
        print(count_dict1)

        count_dict2 = Counter(nums2)
        print(count_dict2)

        res = [0, 0]

        for key in count_dict1:
            if key in count_dict2:
                res[0] += count_dict1[key]

        for key in count_dict2:
            if key in count_dict1:
                res[1] += count_dict2[key]

        return res