from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_set = {i for i in range(1, n + 1)}

        for num in hash_set:
            if num not in nums:
                return num

        return 0