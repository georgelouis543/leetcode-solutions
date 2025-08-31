from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        hash_map = {}
        i = 0

        for c in arr:
            if c not in hash_map:
                hash_map[c] = 1

            else:
                hash_map[c] += 1

        print(hash_map)

        for key in hash_map:
            if hash_map[key] == 1:
                if i == k - 1:
                    return key
                else:
                    i += 1

        return ""
