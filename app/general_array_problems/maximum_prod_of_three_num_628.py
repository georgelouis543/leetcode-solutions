from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # In cases where there are negative numbers,
        # the product of the two smallest (negative)
        # numbers and the largest positive number may
        # yield the maximum product.

        return max(
            nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3],
            nums[0] * nums[1] * nums[len(nums) - 1]
        )
