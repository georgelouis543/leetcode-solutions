class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n > 0:
            digit_str = str(n)
            summ = 0
            for i in digit_str:
                summ += int(i) ** 2

            if summ == 1:
                return True

            if summ in seen:
                return False

            seen.add(summ)
            n = summ

        return False
