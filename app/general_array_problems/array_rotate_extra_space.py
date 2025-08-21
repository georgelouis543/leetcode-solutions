from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out_list = [0] * len(nums)
        n = len(nums)

        if k > len(nums):
            k = k % len(nums)

        out_list[0: k] = nums[n - k: n + 1]
        out_list[k: n] = nums[0: n - k]
        print(out_list)

        for i in range(0, len(out_list)):
            nums[i] = out_list[i]

        return None
