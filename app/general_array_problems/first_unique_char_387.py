class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        for i in range(0, len(s)):
            if s[i] in hash_map:
                hash_map[s[i]].append(i)
            else:
                hash_map[s[i]] = [i]

        print(hash_map)

        for key in hash_map:
            if len(hash_map[key]) == 1:
                return hash_map[key][0]

        return -1
