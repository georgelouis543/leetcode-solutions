from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = ""

        if len(nums) <= 1:
            return True

        i = 0
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] != nums[i + 1]:
                if nums[i + 1] > nums[i]:
                    direction = "increasing"
                else:
                    direction = "decreasing"
                break
            i += 1

        print(direction)

        is_monotonic = False

        if direction == "increasing":
            for i in range(1, len(nums)):
                if nums[i] >= nums[i - 1]:
                    is_monotonic = True
                else:
                    return False

        elif direction == "decreasing":
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    is_monotonic = True
                else:
                    return False

        else:
            return True

        return is_monotonic





