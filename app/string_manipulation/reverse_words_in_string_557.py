class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        print(s)

        for i in range(0, len(s)):
            j = 0
            k = len(s[i]) - 1
            word = list(s[i])
            while j <= k:
                word[j], word[k] = word[k], word[j]
                j += 1
                k -= 1

            s[i] = "".join(word)

        print(s)

        return " ".join(s)