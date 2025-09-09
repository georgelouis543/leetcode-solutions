from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxx_diff = float("-inf")

        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            maxx_diff = max(maxx_diff, curr_diff)

        print(maxx_diff)

        if maxx_diff == float("-inf"): return 0

        return maxx_diff
