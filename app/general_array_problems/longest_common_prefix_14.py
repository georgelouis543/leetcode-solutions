from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for i in range(1, len(strs)):
            curr_common = ""
            for j in range(0, min(len(prefix), len(strs[i]))):
                if prefix[j] == strs[i][j]:
                    curr_common += prefix[j]
                else:
                    break
            prefix = curr_common

        if not prefix:
            return ""
        return prefix