def isBadVersion(version: int) -> bool:
    if version == 8:
        return True
    return False

def firstBadVersion(self, n: int) -> int:
    l = 0
    r = n

    while l < r:
        m = (l + r) // 2

        if not isBadVersion(m):
            l = m + 1
        else:
            r = m

    return r