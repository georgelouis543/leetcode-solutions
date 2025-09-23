from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0

        i = 0
        while i < len(nums) - 1:
            summ += min(nums[i], nums[i + 1])

            i += 2


        return summ