class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        is_monotone_inc = False

        if n <= 10:
            return n - 1

        for i in range(n, -1, -1):
            digit = str(i)
            for j in range(1, len(digit)):
                if int(digit[j - 1]) <= int(digit[j]):
                    is_monotone_inc = True
                else:
                    is_monotone_inc = False
                    break

            if is_monotone_inc:
                return int(digit)

        return 0



