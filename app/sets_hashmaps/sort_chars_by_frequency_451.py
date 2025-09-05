from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = Counter(s)
        print(count_dict)
        res = ""

        for key, freq in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
            res += key * freq
        print(res)

        return res
