class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        t_p1 = abs(x - z)
        t_p2 = abs(y - z)

        print(t_p1, t_p2)

        if t_p1 > t_p2:
            return 2
        elif t_p1 == t_p2:
            return 0
        else:
            return 1