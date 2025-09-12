from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash_map_arr = {}

        for num in arr:
            if num in hash_map_arr:
                hash_map_arr[num] += 1
            else:
                hash_map_arr[num] = 1

        print(hash_map_arr)

        hash_map_target = {}

        for num in target:
            if num in hash_map_target:
                hash_map_target[num] += 1
            else:
                hash_map_target[num] = 1

        print(hash_map_target)

        return hash_map_target == hash_map_arr
