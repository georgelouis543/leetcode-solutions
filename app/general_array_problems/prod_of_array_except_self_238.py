from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        curr_prod = 1
        pre[0] = curr_prod
        for i in range(1, n):
            curr_prod = curr_prod * nums[i - 1]
            pre[i] = curr_prod

        curr_prod = 1
        post[n - 1] = 1
        i = n - 2
        while i >= 0:
            curr_prod = curr_prod * nums[i + 1]
            post[i] = curr_prod
            i -= 1

        return [post[i] * pre[i] for i in range(0, n)]
