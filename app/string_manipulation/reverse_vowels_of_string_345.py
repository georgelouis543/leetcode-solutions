class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        s_list = [c for c in s]
        print(s_list)

        i, j = 0, len(s_list) - 1

        while i < j:

            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

            elif s_list[i] in vowels and s_list[j] not in vowels:
                j -= 1

            elif s_list[i] not in vowels and s_list[j] in vowels:
                i += 1

            else:
                i += 1
                j -= 1

        print(s_list)

        return "".join(s_list)
