from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        print(hash_map)
        print(len(hash_map))

        i = 0
        for key in hash_map:
            nums[i] = key
            i += 1

        print(nums)

        return i

