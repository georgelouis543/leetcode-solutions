from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        print(chars)
        i = 0
        j = 0
        char = ""
        counter = 1

        if len(chars) <= 1:
            return 1

        while j < len(chars):
            char = chars[j]
            counter = 1

            while (j < len(chars) - 1) and (chars[j] == chars[j + 1]):
                counter += 1
                j += 1

            print(char, counter)

            chars[i] = char
            i += 1

            if counter > 1:
                for digit in str(counter):
                    chars[i] = digit
                    i += 1

            j += 1

        print(i)
        print(chars)

        return i
