from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for num in nums1_set:
            if num in nums2_set:
                res.append(num)

        return res