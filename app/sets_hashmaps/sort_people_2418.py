from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_map = {}
        res = []
        for i in range(0, len(names)):
            hash_map[heights[i]] = names[i]

        for key, val in sorted(hash_map.items(), reverse=True):
            res.append(val)

        return res
