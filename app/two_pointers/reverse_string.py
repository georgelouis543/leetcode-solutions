def reverse_string(s: str):
    s_list = [i for i in s]
    i = 0
    j = len(s_list) - 1

    while i < j:
        s_list[i], s_list[j] = s_list[j], s_list[i]
        i += 1
        j -= 1
    return s_list


print(reverse_string("there"))