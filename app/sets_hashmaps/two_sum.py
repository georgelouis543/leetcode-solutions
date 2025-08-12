def two_sum(
        nums: list[int],
        target: int
):
    hash_map = {}
    # Solve for y
    # y = target - x

    for idx, x in enumerate(nums):
        y = target - x

        if x in hash_map:
            return [hash_map[x], idx]

        else:
            hash_map[y] = idx


    return [-1, -1]


print(two_sum([2,7,11,15], 9))