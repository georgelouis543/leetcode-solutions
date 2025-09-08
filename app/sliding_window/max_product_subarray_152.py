from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max = 1, 1
        max_prod = max(nums)

        for num in nums:
            if num == 0:
                curr_min, curr_max = 1, 1
                continue

            temp = curr_max * num
            curr_max = max(num * curr_min, num * curr_max,
                           num)  # consider [-1, 8], num * curr_min = -8, num * curr_max = -8, in which case num = 8 is the maximum
            curr_min = min(num * curr_min, temp, num)
            max_prod = max(max_prod, curr_max)

        return max_prod
