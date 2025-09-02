from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return curr_sum

                elif curr_sum < target:
                    lo += 1

                else:
                    hi -= 1

        return closest_sum

