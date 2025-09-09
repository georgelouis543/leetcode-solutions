from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Kadane's algorithm
        maxx_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            maxx_sum = max(curr_sum, maxx_sum)

            if curr_sum < 0:
                curr_sum = 0

        return maxx_sum
