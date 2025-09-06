from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_dict_s = Counter(s)
        count_dict_t = Counter(t)

        print(count_dict_s)
        print(count_dict_t)

        for key in count_dict_t:
            if key not in count_dict_s:
                return key
            elif key in count_dict_s:
                if count_dict_t[key] > count_dict_s[key]:
                    return key

        return ""
