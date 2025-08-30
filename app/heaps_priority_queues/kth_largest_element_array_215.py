import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums) # Max Heap

        for _ in range(0, k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)