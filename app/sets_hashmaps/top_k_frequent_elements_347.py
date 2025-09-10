from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        print(count_dict)

        for key in count_dict:
            freq[count_dict[key]].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res