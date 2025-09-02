class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_map = {}

        for c in s:
            if c in hash_map:
                return c
            else:
                hash_map[c] = True

        return ""