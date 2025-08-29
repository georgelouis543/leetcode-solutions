class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = False
        stones_to_be_picked = 10
        i = 0

        stones_available = n

        while stones_available >= stones_to_be_picked:
            print(stones_available)
            if i % 2 == 0:
                alice_turn = True
            if i % 2 != 0:
                alice_turn = False

            i += 1
            stones_available = stones_available - stones_to_be_picked
            stones_to_be_picked -= 1

        print(alice_turn)
        print(stones_available)

        return alice_turn
