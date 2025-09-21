from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = [0] * (len(nums1) + len(nums2))

        i = 0
        j = 0
        k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1

            k += 1

        while i < len(nums1):
            res[k] = nums1[i]
            i += 1
            k += 1

        while j < len(nums2):
            res[k] = nums2[j]
            j += 1
            k += 1

        n = len(res)
        if n % 2 == 1:
            return float(res[n // 2])
        else:
            return (res[n // 2 - 1] + res[n // 2]) / 2
