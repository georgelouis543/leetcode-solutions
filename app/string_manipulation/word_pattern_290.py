class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        reverse_map = {}

        word_list = s.split(" ")
        print(word_list)

        if len(word_list) > len(pattern) or len(pattern) > len(word_list):
            return False

        for i in range(0, len(pattern)):
            if pattern[i] in hash_map:
                if hash_map[pattern[i]] != word_list[i]:  # Checking if the key is already mapped to a different word
                    return False

            else:
                if word_list[i] in reverse_map:  # checking if the value is already mapped to a different key
                    return False

                hash_map[pattern[i]] = word_list[i]
                reverse_map[word_list[i]] = pattern[i]

        return True