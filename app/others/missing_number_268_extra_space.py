from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_set = set(nums)

        for i in range(1, n + 1):
            if i not in hash_set:
                return i

        return 0


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2 # n(n + 1)/2

        return expected - sum(nums)