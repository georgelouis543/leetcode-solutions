from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0

        while i < len(nums):
            num = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            nums[j] = num
            i += 1
            j += 1

        return j
