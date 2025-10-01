class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles_drunk = 0
        empty_bottles = 0
        n = numBottles

        while n > 0:
            total_bottles_drunk += n
            empty_bottles += n
            n = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange

        return total_bottles_drunk
