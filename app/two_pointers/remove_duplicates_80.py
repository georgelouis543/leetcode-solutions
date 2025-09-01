from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        j = 2
        k = 0

        for i in range(2, len(nums)):
            if nums[k] != nums[i]:
                nums[j] = nums[i]

                k += 1
                j += 1

        print(j)

        return j



