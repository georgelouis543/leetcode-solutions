class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_jewels = 0

        for i in stones:
            if i in jewels:
                num_jewels += 1

        return num_jewels
