import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        for i in range(0, len(nums)):
            nums[i] = -int(nums[i])

        heapq.heapify(nums)

        for _ in range(0, k - 1):
            heapq.heappop(nums)

        return str(-heapq.heappop(nums))