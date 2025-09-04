from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_set = set(nums)

        for i in range(1, n + 1):
            if i not in hash_set:
                return i

        return 0