class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_set = set()
        l = 0
        longest = float('-inf')

        if len(s) <= 0:
            return 0

        elif len(s) == 1:
            return 1

        for r in range(0, len(s)):

            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1

            curr_window_length = (r - l) + 1
            longest = max(longest, curr_window_length)
            window_set.add(s[r])

        return longest