from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        maxx_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            maxx_sum = max(maxx_sum, curr_sum)

        return maxx_sum
