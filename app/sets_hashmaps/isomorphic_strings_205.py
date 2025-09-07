class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        reverse_map = {}

        for i in range(0, len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = t[i]

        for i in range(0, len(t)):
            if t[i] not in reverse_map:
                reverse_map[t[i]] = s[i]

        print(hash_map)
        temp_t = ""
        for c in s:
            temp_t += hash_map[c]

        print(reverse_map)
        temp_s = ""
        for c in t:
            temp_s += reverse_map[c]

        print(temp_t)
        print(temp_s)

        if temp_t == t and temp_s == s:
            return True

        return False



