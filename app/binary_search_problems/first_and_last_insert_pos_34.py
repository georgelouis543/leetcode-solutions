from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        # Move right to find the last insert position
        while l <= r:
            mid = (l + r) // 2

            if target >= nums[mid]:
                if target == nums[mid]:
                    last = mid

                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        # Move Left to find the first insert position
        while l <= r:
            mid = (l + r) // 2

            if target <= nums[mid]:
                if target == nums[mid]:
                    first = mid

                r = mid - 1

            elif target > nums[mid]:
                l = mid + 1

        return [first, last]


