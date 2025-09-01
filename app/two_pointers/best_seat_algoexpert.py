def bestSeat(seats):
    # Write your code here.
    counter = 0
    max_zeros = float('-inf')
    i = 0
    start = -1
    end = -1

    best_seat = -1

    while i < len(seats):
        counter = 0

        if seats[i] == 0:
            counter = 1
            start = i
            while i < len(seats) - 1 and seats[i] == seats[i + 1]:
                counter += 1
                i += 1
            end = i

        print(start, end)
        if counter > max_zeros:
            max_zeros = max(counter, max_zeros)
            best_seat = (start + end) // 2
            print(best_seat)

        i += 1

    return best_seat
