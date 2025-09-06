from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = len(nums) - 1
            while j > i:
                if abs(nums[j] - nums[i]) == k:
                    counter += 1
                    break

                j -= 1

        return counter