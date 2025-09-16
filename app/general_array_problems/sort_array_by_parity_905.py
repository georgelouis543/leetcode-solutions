from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)

        j = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                res[j] = nums[i]
                j += 1

        for i in range(0, len(nums)):
            if nums[i] % 2 != 0:
                res[j] = nums[i]
                j += 1

        return res
