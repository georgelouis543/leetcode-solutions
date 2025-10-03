from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        maxArr = [0] * n
        minArr = [0] * n

        currMax = float('-inf')
        for idx, num in enumerate(nums):
            currMax = max(currMax, num)
            maxArr[idx] = currMax

        print(maxArr)

        currMin = float('inf')
        r = len(nums) - 1
        while r >= 0:
            currMin = min(currMin, nums[r])
            minArr[r] = currMin
            r -= 1

        print(minArr)
        disjoint_idx = 0
        for i in range(1, len(nums)):
            if minArr[i] >= maxArr[i - 1]:
                disjoint_idx = i
                break

        print(disjoint_idx)
        return disjoint_idx

