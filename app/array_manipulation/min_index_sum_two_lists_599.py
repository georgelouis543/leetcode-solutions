from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_index = float('inf')

        hash_map1 = {}
        for idx, val in enumerate(list1):
            hash_map1[val] = idx

        hash_map2 = {}
        for idx, val in enumerate(list2):
            hash_map2[val] = idx

        print(hash_map1)
        print(hash_map2)

        for key in hash_map1:
            if key in hash_map2:
                curr_min_index = hash_map1[key] + hash_map2[key]
                if curr_min_index <= min_index:
                    min_index = curr_min_index

        print(min_index)

        for key in hash_map1:
            if key in hash_map2:
                if hash_map1[key] + hash_map2[key] == min_index:
                    res.append(key)


        return res