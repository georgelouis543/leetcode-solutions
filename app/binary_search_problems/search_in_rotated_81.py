from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0

        for idx, num in enumerate(nums):
            if idx < len(nums) - 1 and nums[idx] > nums[idx + 1]:
                start = idx + 1

        print(start)

        l, r = 0, start - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                l += 1
            else:
                r -= 1

        l, r = start, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                l += 1
            else:
                r -= 1

        return False