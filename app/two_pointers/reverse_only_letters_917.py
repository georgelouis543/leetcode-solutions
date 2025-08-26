class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = {
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        }

        temp = [c for c in s]
        print(temp)

        i = 0
        j = len(s) - 1

        while i < j:
            if temp[i] in letters and temp[j] in letters:
                temp[i], temp[j] = temp[j], temp[i]
                i += 1
                j -= 1

            elif temp[i] in letters and temp[j] not in letters:
                j -= 1

            elif temp[i] not in letters and temp[j] in letters:
                i += 1

            else:
                i += 1
                j -= 1

        print(temp)

        s = ''.join(temp)

        return s