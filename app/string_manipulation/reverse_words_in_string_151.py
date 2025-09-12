class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        print(s_list)

        i = 0
        j = len(s_list) - 1

        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]

            i += 1
            j -= 1

        print(s_list)

        return " ".join(s_list)
