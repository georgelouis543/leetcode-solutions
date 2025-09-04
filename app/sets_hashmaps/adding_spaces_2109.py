from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        spaces = set(spaces)

        for i in range(0, len(s)):
            if i in spaces:
                res += " " + s[i]
            else:
                res += s[i]

        print(res)

        return res
