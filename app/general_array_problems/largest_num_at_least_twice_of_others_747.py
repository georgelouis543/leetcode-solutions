from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        maxx = max(nums)
        idx_maxx = -1
        maxx_nums = float('-inf')

        for idx, num in enumerate(nums):
            if num > maxx_nums:
                maxx_nums = num
                idx_maxx = idx

        for num in nums:
            if num == maxx:
                continue
            if maxx < 2 * num:
                return -1

        return idx_maxx
