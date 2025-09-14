from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comp_func(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(comp_func), reverse=True)

        return ''.join(nums).lstrip('0') or '0'
