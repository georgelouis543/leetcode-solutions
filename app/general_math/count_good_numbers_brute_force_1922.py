class Solution:
    def countGoodNumbers(self, n: int) -> int:
        digit_string = ""
        count = 0

        for i in range(pow(10, n - 1) + 1, pow(10, n)):
            dig_str = str(i)
            j = 0
            flag = True
            for dig in dig_str:
                if j % 2 == 0 and int(dig) % 2 != 0:
                    flag = False
                    break

                if j % 2 == 1 and int(dig) % 2 != 1:
                    flag = False
                    break

                j += 1

            if flag:
                count += 1

        return count
