from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        n = len(nums)
        i = 0

        for idx, num in enumerate(nums):
            if num in hash_map:
                hash_map[num].append(idx)
            else:
                hash_map[num] = [idx]

        print(hash_map)

        for key in hash_map:
            for i in range(1, len(hash_map[key])):
                if abs(hash_map[key][i] - hash_map[key][i - 1]) <= k:
                    return True

        return False
