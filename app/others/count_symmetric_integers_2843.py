class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0

        for i in range(low, high + 1):
            num_string = str(i)

            if len(num_string) % 2 == 0:
                sum1 = 0
                sum2 = 0
                n = len(num_string) // 2

                for j in range(0, n):
                    sum1 += int(num_string[j])

                for k in range(n, len(num_string)):
                    sum2 += int(num_string[k])

                if sum1 == sum2:
                    counter += 1

        print(counter)
        return counter

