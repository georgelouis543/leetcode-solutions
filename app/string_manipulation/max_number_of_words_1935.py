class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split(" ")
        print(text_list)

        count = 0

        for word in text_list:
            flag = True
            for c in brokenLetters:
                if c in word:
                    flag = False
                    break
            if flag:
                count += 1

        print(count)

        return count
