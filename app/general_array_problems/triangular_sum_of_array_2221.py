from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = []

        for i in range(1, len(nums)):
            res.append((nums[i] + nums[i - 1]) % 10)

        print(res)

        while len(res) > 1:
            newRes = []
            for j in range(1, len(res)):
                currSum = (res[j - 1] + res[j]) % 10
                newRes.append(currSum)

            res = newRes

        print(res)
        return res[0]
