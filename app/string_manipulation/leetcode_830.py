class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = 0
        start = 0
        end = 0
        i = 0
        out_list = []

        while i < (len(s) - 1):
            count = 0
            end = 0
            start = i

            while i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
                i += 1
            end = i

            print(count)
            if count >= 2:
                print(s[i])
                print(i)
                print(len(s) - i)
                out_list.append([start, end])

            i += 1

        print(out_list)

        return out_list
