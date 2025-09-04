from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_index = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if l == r:
                min_index = l
                break

            elif nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

        return nums[min_index]