from typing import List
# O(n*logn) time complexity

# The minimum difference possible is obtained by removing three elements between the three smallest and three largest values in the array.

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        min_diff = float('inf')
        print(nums)

        if len(nums) <= 4:
            return 0

        for l in range(0, 4):
            r = len(nums) - 4 + l

            min_diff = min(min_diff, nums[r] - nums[l])

        return min_diff